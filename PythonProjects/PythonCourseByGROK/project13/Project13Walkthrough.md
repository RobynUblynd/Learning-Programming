Below is a detailed walkthrough for **Project 13: Modules and Code Organization**, formatted similarly to the `Project10Walkthrough.md`. This guide will help you split the bank account system from Project 12 into separate modules (files) for better organization and reusability. By the end, you’ll have a structured project with a module for bank account classes and a main script that imports and uses these classes.

---

## Objective
- Learn how to organize Python code into **modules** for better structure and reusability.
- Practice **importing** classes from one module into another.
- Understand how to separate concerns by keeping class definitions in one file and usage in another.

## Task
Modify the bank account system from Project 12 to:
1. Create a module named `accounts.py` that contains the `BankAccount`, `SavingsAccount`, and `CheckingAccount` classes.
2. Create a `main.py` file that imports these classes from the `accounts` module and uses them to perform operations like deposits, withdrawals, and interest additions.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Set up your workspace to keep your code organized, following the course’s structure.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder containing all your course projects.  
  - **How**: If you haven’t created it yet, open PyCharm, go to **File > New Project**, name it `PythonCourse`, select a location (e.g., Desktop), and click **Create**. If it already exists, open it via **File > Open** and select the `PythonCourse` directory.  
  - **Why**: Provides a central location for all projects.

- **Subfolder for Project 13 (`project13/`)**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click the `PythonCourse` directory, select **New > Directory**, and name it `project13`.  
  - **Why**: Keeps Project 13 separate from other projects for clarity.

- **Python Files (`accounts.py` and `main.py`)**  
  - **What**: Two files—one for the bank account classes (`accounts.py`) and one for the main script (`main.py`).  
  - **How**: Right-click the `project13/` folder, choose **New > Python File**, and create `accounts.py`. Repeat to create `main.py`.  
  - **Why**: Separates class definitions from the code that uses them, improving organization.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
├── project12/
│   └── main.py
└── project13/
    ├── accounts.py
    └── main.py
```

---

### Step 2: Create the `accounts.py` Module
Define the bank account classes in a separate module for reusability.

- **What**: A Python file (`accounts.py`) containing the `BankAccount`, `SavingsAccount`, and `CheckingAccount` classes.  
- **How**: Open `accounts.py` in the `project13/` folder and add the following code:  
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
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Overdraft limit exceeded!")
        self.balance -= amount
        return f"Withdrew ${amount}. Balance: ${self.balance}"
```
- **Why**:  
  - **Modularity**: By placing the classes in a separate file, you can reuse them in other projects or scripts without copying code.  
  - **Organization**: Keeps the main script clean and focused on usage rather than definitions.  
  - **Reusability**: Other parts of the program or future projects can import and use these classes easily.

---

### Step 3: Create the `main.py` Script
Import the classes from `accounts.py` and use them to perform operations.

- **What**: A Python file (`main.py`) that imports the bank account classes and tests them with sample operations.  
- **How**: Open `main.py` in the `project13/` folder and add the following code:  
```python
from accounts import BankAccount, SavingsAccount, CheckingAccount

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
  - **Importing**: `from accounts import BankAccount, SavingsAccount, CheckingAccount` brings the classes into `main.py` for use.  
  - **Testing**: The try-except blocks test various operations, catching and displaying any errors, just like in Project 12.  
  - **Separation of Concerns**: `main.py` focuses on using the classes, while `accounts.py` focuses on defining them.

---

### Step 4: Run and Test the Code
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
  - **Modularity**: Ensure that `main.py` correctly imports and uses the classes from `accounts.py`.

- **Why Test?**: Verifies that the classes work as expected when imported and used in a separate file.

---

### Step 5: Commit Your Changes Using Git
Save your work with Git to track your progress.

- **Initialize Git (If Not Done)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Enables version control for your project.

- **Commit Your Code**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check both `accounts.py` and `main.py`, enter a message like "Completed Project 13: Modules and Code Organization", and click **Commit**.  
  - **Why**: Records your completion of Project 13 for future reference.

---

## What You’ve Learned
- **Modules**: Created a separate Python file (`accounts.py`) to hold class definitions.  
- **Importing**: Used `from accounts import ...` to bring classes into `main.py`.  
- **Code Organization**: Separated class definitions from usage, making the code cleaner and more maintainable.  
- **Reusability**: Demonstrated how modules can be reused across different parts of a program or in other projects.

---

## Extra Challenges
Want to enhance your project? Try these:  
- **Add a New Account Type**: Create another account class (e.g., `CreditCardAccount`) in `accounts.py` and test it in `main.py`.  
- **Create a Module for Utilities**: Add a new module (e.g., `utils.py`) with helper functions (like currency formatting) and import it into `main.py`.  
- **Refactor Error Handling**: Move error handling logic into a separate function to clean up the main script.

---

## Next Steps
- Move on to **Project 14: List Comprehensions with Transactions** to learn more advanced Python features.  
- Continue using Git to track your progress after each project.

You’ve now organized your bank account system into modules, improving your code structure and reusability—great job!