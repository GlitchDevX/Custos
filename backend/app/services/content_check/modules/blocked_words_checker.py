from app.services.metrics.metrics_counter import count_metric
from .content_check_module import ContentCheckModule
import re
import urllib.request
from ....utils.singleton_meta import SingletonMeta
import json
from typing import List

class ProfanityList(metaclass=SingletonMeta):
    profanities = List[str]
    _file_path = "data/profanity_words.json"

    def __init__(self):
        raw_json: str
        try:
            response = urllib.request.urlopen("https://raw.githubusercontent.com/zacanger/profane-words/refs/heads/master/words.json")
            raw_json = response.read().decode('utf-8')
            self._update_file(raw_json)
        except Exception as err:
            print("Failed to get newest blocked words, will read from file\nException:", err)
            raw_json = self._read_file()

        self.profanities = json.loads(raw_json)

    def _read_file(self):
        with open(self._file_path, encoding="utf-8") as file:
            return file.read()

    def _update_file(self, domains_raw):
        with open(self._file_path, "w", encoding="utf-8") as file:
            file.write(domains_raw)

class BlockedWordsContentChecker(ContentCheckModule):
    flag_name = "blocked_word"
    profanity_list = ProfanityList()

    def execute_check(self, content, **kwargs):
        blocked_words = list(set(kwargs.get("config").get("blockedWords") + self.profanity_list.profanities))
        pattern = re.compile(
            r"(" + "|".join(
                r"\b" + re.escape(w) + r"\b" if len(w) <= 3 else re.escape(w)
                for w in sorted(blocked_words, key=len, reverse=True)
            ) + r")",
            re.IGNORECASE
        )
        
        has_blocked_word = False
        
        def censor_match(match):
            nonlocal has_blocked_word
            has_blocked_word = True
            return '*' * len(match.group(0))

        censored_content = pattern.sub(censor_match, content)

        if has_blocked_word:
            count_metric('REALTIME_BLOCKED_WORD_DETECTED')

        return self.flag_name, has_blocked_word, censored_content
