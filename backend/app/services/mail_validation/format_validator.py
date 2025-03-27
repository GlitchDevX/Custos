from .validation_result import ValidationResult
from .validator_module import ValidatorModule


class FormatValidator(ValidatorModule):

    def execute_check(self, email) -> ValidationResult:
        pass
        # impl regex logic 