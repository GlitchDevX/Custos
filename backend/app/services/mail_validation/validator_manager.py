from typing import List

from .validator_module import ValidatorModule
from .validation_result import ValidationResult
from .mailserver_validator import MailserverValidator
from .spamlist_validator import SpamlistValidator
from .format_validator import FormatValidator


class ValidatorManager:
    validators: List[ValidatorModule] = []

    def __init__(self):
        #TODO: Check if is enables in config here
        self.validators.append(FormatValidator())
        self.validators.append(SpamlistValidator())
        self.validators.append(MailserverValidator())

    def evaluate_results(results: List[ValidationResult]):
        # build response body here
        if len(results) == 0:
            return 'ok'
        
        return results[0].text

    def validate_mail(self, mail):
        results: List[ValidationResult] = []
        for validator in self.validators:
            result = validator.execute_check(mail)
            if not result.passed:
                break
        
        return self.evaluate_results(results)
