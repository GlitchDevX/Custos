from typing import List

from app.config_reader import ConfigReader

from .validation_result import ValidationResult
from .modules.validator_module import ValidatorModule
from .modules.mailserver_validator import MailserverValidator
from .modules.disposable_validator import DisposableValidator
from .modules.format_validator import FormatValidator


class ValidatorManager:
    validators: List[ValidatorModule] = []

    def __init__(self):
        self.config = ConfigReader("mail_validation")

        if self.config.get("formatCheck"):
            self.validators.append(FormatValidator())
        
        if self.config.get("disposableCheck"):
            self.validators.append(DisposableValidator(self.config))
        
        if self.config.get("mxRecordCheck"):
            self.validators.append(MailserverValidator(self.config))

    def _evaluate_result(_, result: ValidationResult):
        if result is None or result.passed:
            return {'code': 'OK'}, 200
        
        return {'code': result.code, 'text': result.text}, 200

    def validate_mail(self, mail):
        result: ValidationResult = None
        for validator in self.validators:
            result = validator.execute_check(mail)
            if not result.passed:
                break

        return self._evaluate_result(result)
