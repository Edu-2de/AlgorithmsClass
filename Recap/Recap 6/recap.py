from abc import ABC, abstractmethod

class Bank_account(ABC):
      @abstractmethod
      def display_values(self):
            pass
    
class Current_account(Bank_account):
      def display_values(self):
            print("Current Account")

class Savings_account(Bank_account):
      def display_values(self):
            print("Savings Account")

account1 = Current_account()
account2 = Savings_account()
account1.display_values()  # Output: Current Account
account2.display_values()  # Output: Savings Account
# This code defines an abstract class Bank_account with an abstract method display_values.
# Two subclasses, Current_account and Savings_account, implement the display_values method.