from abc import ABC, abstractmethod

class Bank_account(ABC):
    @abstractmethod
    def display_values(self):
        pass