from app.services.metrics.metrics_counter import count_metric
from typing import List

from app.utils.common_responses import ENDPOINT_DISABLED

from ...config_reader import ConfigReader

from .validation_result import ValidationResult
from .modules.validator_module import ValidatorModule
from .modules.mailserver_validator import MailserverValidator
from .modules.disposable_validator import DisposableValidator
from .modules.format_validator import FormatValidator


class ValidatorManager:
    """
    A class to manage email validation using various validators.
    This class initializes different validators and orchestrates the validation process.
    """
    validators: List[tuple[str, ValidatorModule]] = []

    def __init__(self):
        self.config = ConfigReader("mail_validation")

        self.validators.append(("formatCheck", FormatValidator()))        
        self.validators.append(("disposableCheck", DisposableValidator(self.config)))
        self.validators.append(("mxRecordCheck", MailserverValidator(self.config)))

    def _evaluate_result(_, result: ValidationResult | None):
        code, text = "OK", ""
        if result is not None or (result and not result.passed):
            code, text = result.code, result.text

        count_metric("MAIL_" + result.code) # type: ignore (type system is not smart enough to understand concatenated literals)
        return {'code': code, 'text': text}, 200

    def validate_mail(self, mail):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED

        result: ValidationResult | None = None
        for (configName, validator) in self.validators:
            if not self.config.get(configName):
                continue

            result = validator.execute_check(mail)
            if not result.passed:
                break

        return self._evaluate_result(result)
