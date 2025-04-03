from typing import List

from ...config_reader import ConfigReader
from .modules.content_check_module import ContentCheckModule
from .modules.url_checker import URLContentChecker


class ContentCheckService:
    content_checks: List[tuple[str, ContentCheckModule]] = []
    config = ConfigReader("content_check")

    def __init__(self):
        self.content_checks.append(("urlCheck", URLContentChecker()))

    def check_content(self, content: str):
        flags, censored_content = [], content
        for (configName, check) in self.content_checks:
            if not self.config.get(configName):
                continue

            result = check.execute_check(content)
            if result[1]:
                flags.append(result[0])
                censored_content = result[2]

        return {"flags": flags, "censored_content": censored_content}
