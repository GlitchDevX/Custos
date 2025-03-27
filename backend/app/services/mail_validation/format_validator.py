from .validation_result import ValidationResult
from .validator_module import ValidatorModule


class FormatValidator(ValidatorModule):

    def execute_check(self, email) -> ValidationResult:
        # impl regex logic 
        return ValidationResult(False, "FORMAT_INVALID", "The email format is invalid")