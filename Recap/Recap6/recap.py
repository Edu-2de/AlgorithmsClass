from abc import ABC, abstractmethod

class Bank_account(ABC):
    @abstractmethod
    def display_values(self):
        pass
    
class Current_account(Bank_account):
      def display_values(self):
        return f"Current Account {self.account_number}: Balance = ${self.balance:.2f}"