from app.services.metrics.metrics_counter import count_metric
from typing import List

from app.utils.common_responses import ENDPOINT_DISABLED
from ...config_reader import ConfigReader
from .modules.content_check_module import ContentCheckModule
from .modules.url_checker import URLContentChecker
from .modules.blocked_words_checker import BlockedWordsContentChecker

class ContentCheckService:
    """
    A service class for checking content against various criteria.
    This class manages different content checks and orchestrates the content validation process.
    """
    
    content_checks: List[tuple[str, ContentCheckModule]] = []
    config = ConfigReader("content_check")

    def __init__(self):
        self.content_checks.append(("urlCheck", URLContentChecker()))
        self.content_checks.append(("blockedWordsCheck", BlockedWordsContentChecker()))

    def check_content(self, content: str):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED

        count_metric('REALTIME_EXECUTED_CHECK')

        flags, censored_content = [], content
        for (configName, check) in self.content_checks:
            if not self.config.get(configName):
                continue

            result = check.execute_check(censored_content, config=self.config)
            if result[1]:
                flags.append(result[0])
                censored_content = result[2]

        return {"flags": flags, "censored_content": censored_content}

