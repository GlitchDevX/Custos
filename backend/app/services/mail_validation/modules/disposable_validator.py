from typing import List
from ..validation_result import ValidationResult
from .validator_module import ValidatorModule
from ..mail_utils import get_domain_from_email

class DisposableValidator(ValidatorModule):

    disposable_domains: List[str] = []

    def __init__(self, config):
        with open('data/disposable_mail_domains.txt') as file:
            self.disposable_domains = file.read().splitlines()
        
        self.disposable_domains.extend(config.get("disposableDomains"))

    def execute_check(self, email):
        domain = get_domain_from_email(email)
        
        if domain in self.disposable_domains:
            return ValidationResult(False, "DISPOSABLE", "Disposable mails are not allowed")
        
        return ValidationResult(True, "OK", "Everything okay")
