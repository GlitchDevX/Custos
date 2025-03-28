from .validation_result import ValidationResult
from .validator_module import ValidatorModule


class MailserverValidator(ValidatorModule):

    def execute_check(self, email):
        # impl mailserver check via dns record domain
        return ValidationResult(False, "NO_MAILSERVER", "The Mailserver is not reachable")