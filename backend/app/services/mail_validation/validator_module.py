from abc import abstractmethod, ABC

class ValidatorModule(ABC):
    
    @abstractmethod
    def execute_check(self, email):
        pass