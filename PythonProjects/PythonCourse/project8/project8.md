#### Project 8: Basic OOP
- **Objective**: Understand object-oriented programming.
- **Task**: Create a `BankAccount` class with:
  1. Attributes: `balance`.
  2. Methods: `deposit(amount)` and `withdraw(amount)`.
  3. Test the class with sample transactions.


- **Example Code**:
- <details>
  <summary>Spoiler</summary>

   ```python
  class BankAccount:
      def __init__(self):
          self.balance = 0
      def deposit(self, amount):
          if amount > 0:
              self.balance += amount
              print(f"Deposited ${amount}. New balance: ${self.balance}")
      def withdraw(self, amount):
          if amount <= self.balance:
              self.balance -= amount
              print(f"Withdrew ${amount}. New balance: ${self.balance}")
          else:
              print("Insufficient funds!")
  account = BankAccount()
  account.deposit(100)
  account.withdraw(50)
  ```
  </details>
  

- **Folder**: `project8/`
