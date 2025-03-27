from typing import List

from flask import json

from .validator_module import ValidatorModule
from .validation_result import ValidationResult
from .mailserver_validator import MailserverValidator
from .disposable_validator import DisposableValidator
from .format_validator import FormatValidator


class ValidatorManager:
    validators: List[ValidatorModule] = []

    def __init__(self):
        #TODO: Check if is enables in config here
        self.validators.append(FormatValidator())
        # self.validators.append(SpamlistValidator())
        # self.validators.append(MailserverValidator())

    def _evaluate_result(_, result: ValidationResult):
        if result is None or result.passed:
            return json.dumps({'code': 'OK'}), 200
        
        return json.dumps({'code': result.code, 'text': result.text}), 400

    def validate_mail(self, mail):
        result: ValidationResult = None
        for validator in self.validators:
            result = validator.execute_check(mail)
            if not result.passed:
                break

        return self._evaluate_result(result)
