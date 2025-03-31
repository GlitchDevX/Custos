from typing import List

from app.config_reader import ConfigReader

from .validation_result import ValidationResult
from .modules.validator_module import ValidatorModule
from .modules.mailserver_validator import MailserverValidator
from .modules.disposable_validator import DisposableValidator
from .modules.format_validator import FormatValidator
from ...models.metric import Metric


class ValidatorManager:
    validators: List[tuple[str, ValidatorModule]] = []

    def __init__(self):
        self.config = ConfigReader("mail_validation")

        self.validators.append(("formatCheck", FormatValidator()))        
        self.validators.append(("disposableCheck", DisposableValidator(self.config)))
        self.validators.append(("mxRecordCheck", MailserverValidator(self.config)))

    def _evaluate_result(_, result: ValidationResult):
        code, text = "OK", ""
        if result is not None or not result.passed:
            code, text = result.code, result.text

        Metric.increase(f"MAIL_{result.code}")
        return {'code': code, 'text': text}, 200

    def validate_mail(self, mail):
        result: ValidationResult = None
        for (configName, validator) in self.validators:
            if not self.config.get(configName):
                continue

            result = validator.execute_check(mail)
            if not result.passed:
                break

        return self._evaluate_result(result)
