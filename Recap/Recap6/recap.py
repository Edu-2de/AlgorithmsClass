from abc import ABC, abstractmethod

class Bank_account(ABC):
      @abstractmethod
      def display_values(self):
            pass
    
class Current_account(Bank_account):
      def display_values(self):
            print("Current Account")