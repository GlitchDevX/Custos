from typing import Literal
from abc import abstractmethod, ABC

class ContentCheckModule(ABC):

    @property
    @abstractmethod
    def flag_name(self):
        return self.flag_name

    @abstractmethod
    def execute_check(self, content: str, **kwargs) -> tuple[str, bool, str]: # flag_name, check_failed, censored
        pass
