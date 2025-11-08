from abc import ABC, abstractmethod

class BaseDriver(ABC):
    @abstractmethod
    def get(self, url: str):
        pass

    @abstractmethod
    def find_element(self, locator_type: str, locator_value: str):
        pass

    @abstractmethod
    def click(self, locator_type: str, locator_value: str):
        pass

    @abstractmethod
    def send_keys(self, locator_type: str, locator_value: str, text: str):
        pass

    @abstractmethod
    def wait_for_element(self, locator_type: str, locator_value: str, timeout: int = 10):
        pass

    @abstractmethod
    def quit(self):
        pass
