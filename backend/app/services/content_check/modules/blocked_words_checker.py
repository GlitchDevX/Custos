from .content_check_module import ContentCheckModule
from ....models.metric import Metric
import re
import urllib.request
from ....utils.singleton_meta import SingletonMeta
import json
from typing import List

class ProfanityList(metaclass=SingletonMeta):
    profanities = List[str]

    def __init__(self):
        response = urllib.request.urlopen("https://raw.githubusercontent.com/zacanger/profane-words/refs/heads/master/words.json")
        raw_data = response.read().decode('utf-8')
        self.profanities = json.loads(raw_data)

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
            Metric.increase(f"CONTENT_BLOCKED_WORD_DETECTED")

        return self.flag_name, has_blocked_word, censored_content
