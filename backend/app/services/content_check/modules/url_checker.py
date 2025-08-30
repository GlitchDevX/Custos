import urllib.request
from http.client import HTTPResponse
from typing import List

from .content_check_module import ContentCheckModule
from ....utils.singleton_meta import SingletonMeta
import re
import urllib
from ....models.metric import Metric

class TopLevelDomainList(metaclass=SingletonMeta):
    top_level_domains = []
    _file_path = "data/top_level_domains.txt"

    def __init__(self):
        _domain_list: List[str]
        try:
            response: HTTPResponse = urllib.request.urlopen("https://data.iana.org/TLD/tlds-alpha-by-domain.txt")
            response_text = response.read().decode("utf-8")
            _domain_list = response_text.splitlines()
            self._update_file(response_text)
        except:
            print("Failed to get newest top level domain list, will read from file")
            _domain_list = self._read_file()

        self._process_and_add_domains(_domain_list)

    def _process_and_add_domains(self, domains: List[str]):
        for domain in domains[1:]: # remove version comment
            self.top_level_domains.append(domain.strip().lower())

    def _read_file(self):
        with open(self._file_path) as file:
            return file.read().splitlines()

    def _update_file(self, domains_raw):
        with open(self._file_path, "w") as file:
            file.write(domains_raw)


class URLContentChecker(ContentCheckModule):
    domain_checker = TopLevelDomainList()
    flag_name = "contains_url"
    pattern = re.compile("((http://|https://)?(www.)?(([a-zA-Z0-9-]){1,}\.){1,127}(?P<domain_ending>[a-zA-Z]{2,6})(/([a-zA-Z-_/.0-9#:?=&;,]*)?)?)",
        re.IGNORECASE,
    )

    def execute_check(self, content, **kwargs):
        censored_content = content
        has_url = False
        matches = self.pattern.finditer(content)
        for m in matches:
            groups = m.groupdict()
            domain_ending = groups['domain_ending']
            if domain_ending in self.domain_checker.top_level_domains:                
                censored_content = ('*' * len(m[0])).join([censored_content[:m.span()[0]], censored_content[m.span()[1]:]])
                has_url = True

        if has_url:
            Metric.increase(f"CONTENT_URL_DETECTED")

        return self.flag_name, has_url, censored_content
