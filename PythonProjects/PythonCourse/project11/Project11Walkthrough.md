Below is a detailed walkthrough for **Project 11: Inheritance in Bank Accounts**, designed to guide you through extending the `BankAccount` class from Project 8 using Python’s object-oriented programming (OOP) inheritance features. This project is beginner-friendly and builds on your prior knowledge, introducing inheritance, method overriding, and the use of `super()`. By the end, you’ll have a working bank account system with specialized account types, tested with sample transactions.

---

## Objective
- Learn how to use **inheritance** in object-oriented programming to extend an existing class.
- Practice creating **derived classes** that inherit and modify behavior from a base class.
- Understand how to use **`super()`** to call base class methods and **override methods** to customize functionality.

## Task
Create a bank account system that:
1. Defines a base `BankAccount` class with basic deposit and withdrawal methods.
2. Creates derived classes `SavingsAccount` (adds interest calculation) and `CheckingAccount` (allows overdraft up to a limit).
3. Tests both classes with sample transactions to demonstrate their unique features.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Set up your workspace to keep your code organized, following the course’s structure.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder containing all your course projects.  
  - **How**: If you haven’t created it yet, open PyCharm, go to **File > New Project**, name it `PythonCourse`, select a location (e.g., Desktop), and click **Create**. If it already exists, open it via **File > Open** and select the `PythonCourse` directory.  
  - **Why**: Provides a central location for all projects.

- **Subfolder for Project 11 (`project11/`)**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click the `PythonCourse` directory, select **New > Directory**, and name it `project11`.  
  - **Why**: Keeps Project 11 separate from other projects for clarity.

- **Python File (`main.py`)**  
  - **What**: The file where you’ll write your code.  
  - **How**: Right-click the `project11/` folder, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a standard name for the main script in Python projects.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
├── project10/
│   └── main.py
└── project11/
    └── main.py
```

---

### Step 2: Define the BankAccount Base Class
Start by creating the foundation of your bank account system—the `BankAccount` class.

- **What**: A base class with basic functionality for managing an account balance.  
- **How**: Open `main.py` in the `project11/` folder and add the following code:  
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. Balance: ${self.balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Balance: ${self.balance}"
        return "Insufficient funds!"
```
- **Why**:  
  - `__init__`: Initializes the balance to 0.  
  - `deposit`: Adds money to the balance if the amount is positive, returning a confirmation message.  
  - `withdraw`: Removes money if sufficient funds are available, otherwise returns an error message.  
  - This class provides the core functionality that `SavingsAccount` and `CheckingAccount` will inherit.

---

### Step 3: Create the SavingsAccount Class
Next, create a derived class that adds savings-specific features.

- **What**: A `SavingsAccount` class that inherits from `BankAccount` and includes interest calculation.  
- **How**: Below the `BankAccount` class in `main.py`, add:  
```python
class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.02  # 2% interest

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Added ${interest:.2f} interest. Balance: ${self.balance:.2f}"
```
- **Why**:  
  - `SavingsAccount(BankAccount)`: Indicates inheritance from `BankAccount`.  
  - `super().__init__()`: Calls the base class constructor to set up the balance.  
  - `interest_rate`: A new attribute specific to savings accounts.  
  - `add_interest`: Calculates 2% interest on the current balance and adds it, formatting the output to two decimal places for readability.  
  - This demonstrates how inheritance lets you reuse `deposit` and `withdraw` while adding new behavior.

---

### Step 4: Create the CheckingAccount Class
Now, create another derived class with checking-specific features.

- **What**: A `CheckingAccount` class that inherits from `BankAccount` and allows overdrafts.  
- **How**: Below the `SavingsAccount` class in `main.py`, add:  
```python
class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_limit = 50

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew ${amount}. Balance: ${self.balance}"
        return "Overdraft limit exceeded!"
```
- **Why**:  
  - `CheckingAccount(BankAccount)`: Inherits from `BankAccount`.  
  - `super().__init__()`: Initializes the base class balance.  
  - `overdraft_limit`: A new attribute allowing withdrawals up to $50 beyond the balance.  
  - `withdraw`: Overrides the base class method to check against `balance + overdraft_limit`, demonstrating method overriding.  
  - This shows how inheritance can modify existing behavior for specific needs.

---

### Step 5: Test the Classes
Finally, test your classes to see inheritance in action.

- **What**: Write code to create instances of both classes and perform sample transactions.  
- **How**: At the bottom of `main.py`, add:  
```python
# Test SavingsAccount
savings = SavingsAccount()
print(savings.deposit(100))
print(savings.add_interest())

# Test CheckingAccount
checking = CheckingAccount()
print(checking.deposit(20))
print(checking.withdraw(60))  # Should allow overdraft
print(checking.withdraw(10))  # Should exceed overdraft limit
```
- **Why**:  
  - **SavingsAccount Test**: Deposits $100, then adds 2% interest ($2), showing the new balance.  
  - **CheckingAccount Test**: Deposits $20, withdraws $60 (allowed since $20 + $50 overdraft = $70), then attempts another $10 withdrawal (fails as it exceeds the limit).  
  - This verifies that inheritance, `super()`, and method overriding work as expected.

**Complete `main.py` Code**:
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. Balance: ${self.balance}"
        return "Invalid deposit amount!"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Balance: ${self.balance}"
        return "Insufficient funds!"

class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate = 0.02  # 2% interest

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Added ${interest:.2f} interest. Balance: ${self.balance:.2f}"

class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_limit = 50

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew ${amount}. Balance: ${self.balance}"
        return "Overdraft limit exceeded!"

# Test SavingsAccount
savings = SavingsAccount()
print(savings.deposit(100))
print(savings.add_interest())

# Test CheckingAccount
checking = CheckingAccount()
print(checking.deposit(20))
print(checking.withdraw(60))  # Should allow overdraft
print(checking.withdraw(10))  # Should exceed overdraft limit
```

---

### Step 6: Run and Test the Code
Ensure your code works as intended.

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button (top-right).  
  - Output appears in the console.

- **Expected Output**:
```
Deposited $100. Balance: $100
Added $2.00 interest. Balance: $102.00
Deposited $20. Balance: $20
Withdrew $60. Balance: $-40
Overdraft limit exceeded!
```

- **Test These Scenarios**:  
  - **SavingsAccount**: Deposit works, interest adds correctly.  
  - **CheckingAccount**: Overdraft within $50 works, beyond fails.  
  - **Inheritance**: Both classes can use `deposit` from `BankAccount`.  
  - **Invalid Input**: Try negative deposits (returns error).

- **Why Test?**: Confirms that each class behaves correctly and inheritance is implemented properly.

---

### Step 7: Commit Your Changes Using Git
Save your work with Git to track your progress.

- **Initialize Git (If Not Done)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Enables version control for your project.

- **Commit Your Code**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, enter a message like "Completed Project 11: Inheritance in Bank Accounts", and click **Commit**.  
  - **Why**: Records your completion of Project 11 for future reference.

---

## What You’ve Learned
- **Inheritance**: Created `SavingsAccount` and `CheckingAccount` that inherit from `BankAccount`.  
- **Method Overriding**: Modified `withdraw` in `CheckingAccount` to allow overdrafts.  
- **super()**: Used to call the base class constructor in derived classes.  
- **OOP Principles**: Reused code efficiently while adding specialized features.

---

## Extra Challenges
Want to enhance your project? Try these:  
- **Transaction History**: Add a list to track all deposits and withdrawals for each account.  
- **Variable Interest**: Allow `SavingsAccount` to set different interest rates.  
- **New Account Type**: Create a `CreditCardAccount` with its own features (e.g., credit limit).  
- **Input Validation**: Add checks for non-numeric amounts in `deposit` and `withdraw`.

---

## Next Steps
- Move on to **Project 12: Error Handling** to learn how to manage errors in your code.  
- Continue using Git to track your progress after each project.

You’ve now built a bank account system using inheritance, expanding your OOP skills in Python—well done!