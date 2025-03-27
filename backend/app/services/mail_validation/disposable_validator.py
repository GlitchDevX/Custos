from .validation_result import ValidationResult
from .validator_module import ValidatorModule


class DisposableValidator(ValidatorModule):

    def execute_check(self, email):
        # impl list logic 
        return ValidationResult(False, "DISPOSABLE", "Disposable mails are not allowed")
