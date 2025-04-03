import urllib.request
from .content_check_module import ContentCheckModule
from ....utils.singleton_meta import SingletonMeta
import re
import urllib
from ....models.metric import Metric

class TopLevelDomainChecker(metaclass=SingletonMeta):
    top_level_domains = []
    def __init__(self):
        _list_raw = urllib.request.urlopen("http://data.iana.org/TLD/tlds-alpha-by-domain.txt")
        for l in _list_raw:
            self.top_level_domains.append(l.decode('utf-8').strip().lower())


class URLContentChecker(ContentCheckModule):
    domain_checker = TopLevelDomainChecker()
    flag_name = "contains_url"
    pattern = re.compile("((http://|https://)?(www.)?(([a-zA-Z0-9-]){2,}\.){1,4}([a-zA-Z]){2,6}(/([a-zA-Z-_/.0-9#:?=&;,]*)?)?)",
        re.IGNORECASE,
    )

    def execute_check(self, content, **kwargs):
        censored_content = content
        has_url = False
        matches = self.pattern.findall(content)
        for m in matches:
            matched_parts = m[0].rsplit(".", 1)
            if matched_parts[-1] in self.domain_checker.top_level_domains:
                censored_content = re.sub(re.escape(m[0]), '*' * len(m[0]), censored_content)
                has_url = True

        if has_url:
            Metric.increase(f"CONTENT_URL_DETECTED")

        return self.flag_name, has_url, censored_content
