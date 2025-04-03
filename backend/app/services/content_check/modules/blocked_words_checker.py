from .content_check_module import ContentCheckModule
from ....models.metric import Metric
import re

class BlockedWordsContentChecker(ContentCheckModule):
    flag_name = "banned_word"

    def execute_check(self, content, **kwargs):
        blocked_words = kwargs.get("config").get("blockedWords")
        censored_content = content.rstrip(",.!?:")
        has_banned_word = False
        
        for s in censored_content.split(" "):
            if s in blocked_words:
                censored_content = re.sub(re.escape(s), '*' * len(s), censored_content)
                has_banned_word = True

        if has_banned_word:
            Metric.increase(f"CONTENT_BANNED_WORD_DETECTED")

        return self.flag_name, has_banned_word, censored_content
