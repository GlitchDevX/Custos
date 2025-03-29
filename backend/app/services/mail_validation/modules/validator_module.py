from abc import abstractmethod, ABC

from ..validation_result import ValidationResult

class ValidatorModule(ABC):

    @abstractmethod
    def execute_check(self, email) -> ValidationResult:
        pass
