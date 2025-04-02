import re
from ..validation_result import ValidationResult
from .validator_module import ValidatorModule


class FormatValidator(ValidatorModule):

    _invalid_result = ValidationResult(False, "FORMAT_INVALID", "The email format is invalid")
    _ok_result = ValidationResult(True, "OK", "Everything okay")

    _regex=re.compile("^[A-z0-9!#$%&'*+\-/=?^_`{|}~.]+@[A-z0-9-.]+\.[A-z0-9]+$")

    def execute_check(self, email: str) -> ValidationResult:
        # impl regex logic 
        if re.match(self._regex, email) is None:
            return self._invalid_result
        return self._ok_result