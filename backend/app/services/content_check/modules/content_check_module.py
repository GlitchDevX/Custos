from abc import abstractmethod, ABC

class ContentCheckModule(ABC):

    @property
    @abstractmethod
    def flag_name(self):
        pass

    @abstractmethod
    def execute_check(self, content):
        pass
