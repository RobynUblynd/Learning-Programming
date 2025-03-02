Below is a detailed walkthrough for **Project 12: Error Handling in Bank Accounts**, formatted similarly to the `Project10Walkthrough.md`. This guide will help you modify the bank account system from Project 11 to include exception handling, making it more robust and user-friendly. By the end, you’ll have a program that gracefully manages errors like invalid deposits or withdrawals.

---

## Objective
- Learn how to use **exceptions** in Python to handle errors gracefully.
- Practice **raising exceptions** for invalid operations in methods.
- Use **try-except blocks** to catch and respond to errors in the main program.

## Task
Modify the bank account system from Project 11 to:
1. Raise exceptions for invalid operations (e.g., depositing a negative amount or withdrawing more than the available balance).
2. Use try-except blocks in the main program to handle these exceptions and provide user-friendly feedback.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Set up your workspace to keep your code organized, following the course’s structure.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder containing all your course projects.  
  - **How**: If you haven’t created it yet, open PyCharm, go to **File > New Project**, name it `PythonCourse`, select a location (e.g., Desktop), and click **Create**. If it already exists, open it via **File > Open** and select the `PythonCourse` directory.  
  - **Why**: Provides a central location for all projects.

- **Subfolder for Project 12 (`project12/`)**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click the `PythonCourse` directory, select **New > Directory**, and name it `project12`.  
  - **Why**: Keeps Project 12 separate from other projects for clarity.

- **Python File (`main.py`)**  
  - **What**: The file where you’ll write your code.  
  - **How**: Right-click the `project12/` folder, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a standard name for the main script in Python projects.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
├── project11/
│   └── main.py
└── project12/
    └── main.py
```

---

### Step 2: Modify the BankAccount Class
Update the base `BankAccount` class to raise exceptions for invalid operations.

- **What**: Adjust the `deposit` and `withdraw` methods to use exceptions instead of returning messages.  
- **How**: Open `main.py` in the `project12/` folder and add the following code:  
```python
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        return f"Deposited ${amount}. Balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        return f"Withdrew ${amount}. Balance: ${self.balance}"
```
- **Why**:  
  - **Deposit**: Raises a `ValueError` if the deposit amount is not positive.  
  - **Withdraw**: Raises a `ValueError` if the withdrawal amount is not positive or exceeds the balance.  
  - Using exceptions allows the program to signal errors explicitly, which can be caught and handled later.

---

### Step 3: Update the SavingsAccount Class
The `SavingsAccount` class from Project 11 adds interest calculation. Since it doesn’t introduce new error-prone operations, we’ll keep it as is for now.

- **What**: Include the `SavingsAccount` class with its `add_interest` method.  
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
  - Inherits from `BankAccount` and adds interest functionality.  
  - No additional error handling is needed here, as the base class handles deposit and withdrawal errors.

---

### Step 4: Update the CheckingAccount Class
Modify the `CheckingAccount` class to handle overdraft limits with exceptions.

- **What**: Adjust the `withdraw` method to raise exceptions for invalid withdrawals.  
- **How**: Below the `SavingsAccount` class in `main.py`, add:  
```python
class CheckingAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_limit = 50

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded!")
        self.balance -= amount
        return f"Withdrew ${amount}. Balance: ${self.balance}"
```
- **Why**:  
  - **Positive Check**: Ensures the withdrawal amount is positive.  
  - **Overdraft Check**: Allows withdrawals up to the overdraft limit (e.g., $50 beyond the balance).  
  - Raises exceptions for invalid amounts or exceeding the overdraft limit.

---

### Step 5: Implement Try-Except Blocks for Testing
Test the classes by performing operations and handling exceptions with try-except blocks.

- **What**: Write code to test both `SavingsAccount` and `CheckingAccount`, catching and displaying errors.  
- **How**: At the bottom of `main.py`, add:  
```python
# Test SavingsAccount
print("Testing SavingsAccount:")
savings = SavingsAccount()
try:
    print(savings.deposit(100))
except ValueError as e:
    print(f"Error: {e}")
try:
    print(savings.add_interest())
except ValueError as e:
    print(f"Error: {e}")
try:
    print(savings.deposit(-10))
except ValueError as e:
    print(f"Error: {e}")
try:
    print(savings.withdraw(50))
except ValueError as e:
    print(f"Error: {e}")
try:
    print(savings.withdraw(200))
except ValueError as e:
    print(f"Error: {e}")

# Test CheckingAccount
print("\nTesting CheckingAccount:")
checking = CheckingAccount()
try:
    print(checking.deposit(20))
except ValueError as e:
    print(f"Error: {e}")
try:
    print(checking.withdraw(30))
except ValueError as e:
    print(f"Error: {e}")
try:
    print(checking.withdraw(45))
except ValueError as e:
    print(f"Error: {e}")
```
- **Why**:  
  - Each operation is wrapped in a `try-except` block to catch `ValueError` exceptions.  
  - **SavingsAccount Tests**:  
    - Deposit $100: Succeeds.  
    - Add interest: Succeeds.  
    - Deposit -10: Fails with "Deposit amount must be positive!"  
    - Withdraw $50: Succeeds.  
    - Withdraw $200: Fails with "Insufficient funds!"  
  - **CheckingAccount Tests**:  
    - Deposit $20: Succeeds.  
    - Withdraw $30: Succeeds (balance becomes -10, within overdraft).  
    - Withdraw $45: Fails with "Overdraft limit exceeded!" (since -10 - 45 = -55 < -50 limit).  
  - This setup ensures the program continues running even when errors occur.

---

### Step 6: Run and Test the Code
Ensure your code works as expected.

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button (top-right).  
  - Output appears in the console.

- **Expected Output**:
```
Testing SavingsAccount:
Deposited $100. Balance: $100
Added $2.00 interest. Balance: $102.00
Error: Deposit amount must be positive!
Withdrew $50. Balance: $52
Error: Insufficient funds!

Testing CheckingAccount:
Deposited $20. Balance: $20
Withdrew $30. Balance: $-10
Error: Overdraft limit exceeded!
```

- **Test These Scenarios**:  
  - **SavingsAccount**: Valid deposits, interest addition, invalid deposits, valid withdrawals, and overdrawing.  
  - **CheckingAccount**: Valid deposits, withdrawals within overdraft, and withdrawals exceeding overdraft.  
  - **Error Handling**: Ensure errors are caught and displayed without crashing the program.

- **Why Test?**: Verifies that exceptions are raised and handled correctly.

---

### Step 7: Commit Your Changes Using Git
Save your work with Git to track your progress.

- **Initialize Git (If Not Done)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Enables version control for your project.

- **Commit Your Code**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, enter a message like "Completed Project 12: Error Handling in Bank Accounts", and click **Commit**.  
  - **Why**: Records your completion of Project 12 for future reference.

---

## What You’ve Learned
- **Raising Exceptions**: Used `raise ValueError` to signal errors in methods.  
- **Catching Exceptions**: Implemented `try-except` blocks to handle errors gracefully.  
- **Object-Oriented Error Handling**: Applied these concepts to a class hierarchy, customizing behavior in derived classes.  
- **Program Robustness**: Ensured the program continues running despite errors.

---

## Extra Challenges
Want to enhance your project? Try these:  
- **Add a Transfer Method**: Implement a method to transfer funds between accounts, handling potential errors.  
- **Handle Non-Numeric Inputs**: Use `TypeError` to handle cases where non-numeric values are passed to methods.  
- **Create a CreditCardAccount**: Add a new account type with its own error handling (e.g., credit limit checks).

---

## Next Steps
- Move on to **Project 13: Modules and Code Organization** to learn how to structure your Python projects.  
- Continue using Git to track your progress after each project.

You’ve now built a more robust bank account system with error handling, strengthening your Python skills—great job!