Below is a detailed walkthrough for **Project 14: List Comprehensions with Transactions**, formatted in a clear and structured style similar to `Project10Walkthrough.md`. This guide will help you enhance a bank account system by adding transaction history and using list comprehensions to analyze transactions. By the end, you’ll have a program that tracks deposits and withdrawals and calculates totals efficiently.

---

## Objective
- Learn how to use **list comprehensions** for efficient data processing.
- Practice storing and managing transaction history in a list of dictionaries.
- Understand how to filter and sum transaction data using list comprehensions.

## Task
Enhance the bank account system to:
1. Store a history of transactions (deposits and withdrawals) as a list of dictionaries in the `BankAccount` class.
2. Use list comprehensions to calculate the total deposits and total withdrawals from the transaction history.
3. Display the transaction history and totals for testing.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Set up your workspace to keep your code organized.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder containing all your course projects.  
  - **How**: If you haven’t created it yet, open PyCharm, go to **File > New Project**, name it `PythonCourse`, select a location (e.g., Desktop), and click **Create**. If it already exists, open it via **File > Open** and select the `PythonCourse` directory.  
  - **Why**: Provides a central location for all projects.

- **Subfolder for Project 14 (`project14/`)**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click the `PythonCourse` directory, select **New > Directory**, and name it `project14`.  
  - **Why**: Keeps Project 14 separate from other projects for clarity.

- **Python Files (`accounts.py` and `main.py`)**  
  - **What**: Two files—one for the bank account classes (`accounts.py`) and one for the main script (`main.py`).  
  - **How**: Right-click the `project14/` folder, choose **New > Python File**, and create `accounts.py`. Repeat to create `main.py`.  
  - **Why**: Separates class definitions from the code that uses them, improving organization.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
├── project13/
│   ├── accounts.py
│   └── main.py
└── project14/
    ├── accounts.py
    └── main.py
```

---

### Step 2: Update the `accounts.py` Module
Modify the `BankAccount` class to include transaction history and methods to analyze it using list comprehensions.

- **What**: Update the `BankAccount` class in `accounts.py` to store transactions and add methods for calculating totals.  
- **How**: Open `accounts.py` in the `project14/` folder and add the following code:  
```python
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []  # List to store transaction history

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance += amount
        self.transactions.append({"type": "deposit", "amount": amount})
        return f"Deposited ${amount}. Balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        self.transactions.append({"type": "withdraw", "amount": amount})
        return f"Withdrew ${amount}. Balance: ${self.balance}"

    def get_total_deposits(self):
        deposits = [t["amount"] for t in self.transactions if t["type"] == "deposit"]
        return sum(deposits)

    def get_total_withdrawals(self):
        withdrawals = [t["amount"] for t in self.transactions if t["type"] == "withdraw"]
        return sum(withdrawals)

    def show_transactions(self):
        for t in self.transactions:
            print(f"{t['type'].capitalize()}: ${t['amount']}")
```
- **Why**:  
  - **Transaction History**: Each deposit and withdrawal adds a dictionary to the `transactions` list with the type and amount.  
  - **List Comprehensions**: `get_total_deposits` and `get_total_withdrawals` use list comprehensions to filter and sum the respective transaction amounts efficiently.  
  - **Show Transactions**: A method to display the transaction history for testing.

**Note**: This walkthrough focuses on the base `BankAccount` class for simplicity. You can extend similar functionality to subclasses like `SavingsAccount` or `CheckingAccount` if needed.

---

### Step 3: Update the `main.py` Script
Import the updated `BankAccount` class and test the new transaction history features.

- **What**: Modify `main.py` to create a `BankAccount`, perform transactions, and display totals using the new methods.  
- **How**: Open `main.py` in the `project14/` folder and add the following code:  
```python
from accounts import BankAccount

# Create a BankAccount instance
account = BankAccount()

# Perform some transactions
try:
    print(account.deposit(100))
    print(account.withdraw(30))
    print(account.deposit(50))
    print(account.withdraw(20))
except ValueError as e:
    print(f"Error: {e}")

# Show transaction history
print("\nTransaction History:")
account.show_transactions()

# Show total deposits and withdrawals
print(f"\nTotal Deposits: ${account.get_total_deposits()}")
print(f"Total Withdrawals: ${account.get_total_withdrawals()}")
```
- **Why**:  
  - **Testing Transactions**: Deposits and withdrawals are performed, with error handling for invalid inputs.  
  - **Displaying History**: The `show_transactions` method prints each transaction.  
  - **Calculating Totals**: The `get_total_deposits` and `get_total_withdrawals` methods calculate and display the totals using list comprehensions.

---

### Step 4: Run and Test the Code
Ensure your code works as expected.

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button (top-right).  
  - Output appears in the console.

- **Expected Output**:
```
Deposited $100. Balance: $100
Withdrew $30. Balance: $70
Deposited $50. Balance: $120
Withdrew $20. Balance: $100

Transaction History:
Deposit: $100
Withdraw: $30
Deposit: $50
Withdraw: $20

Total Deposits: $150
Total Withdrawals: $50
```

- **Test These Scenarios**:  
  - **Valid Transactions**: Ensure deposits and withdrawals update the balance and transaction history correctly.  
  - **Totals Calculation**: Verify that total deposits and withdrawals are calculated accurately.  
  - **Error Handling**: Test invalid operations (e.g., withdrawing more than the balance or depositing a negative amount) to ensure errors are caught.

- **Why Test?**: Confirms that the transaction history is recorded and analyzed correctly.

---

### Step 5: Commit Your Changes Using Git
Save your work with Git to track your progress.

- **Initialize Git (If Not Done)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Enables version control for your project.

- **Commit Your Code**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check both `accounts.py` and `main.py`, enter a message like "Completed Project 14: List Comprehensions with Transactions", and click **Commit**.  
  - **Why**: Records your completion of Project 14 for future reference.

---

## What You’ve Learned
- **List Comprehensions**: Used to filter and sum transaction amounts efficiently.  
- **Transaction History**: Stored transactions in a list of dictionaries for easy access and analysis.  
- **Code Organization**: Continued using modules to separate class definitions from usage.  
- **Data Analysis**: Demonstrated how to extract and calculate meaningful data from a list of records.

---

## Extra Challenges
Want to enhance your project? Try these:  
- **Add Transaction Dates**: Include a timestamp for each transaction using `datetime` and display it in the history.  
- **Filter by Type**: Create methods to return lists of only deposits or only withdrawals using list comprehensions.  
- **Calculate Net Balance**: Use list comprehensions to compute the net balance (total deposits minus total withdrawals).

---

## Next Steps
- Move on to **Project 15: Working with JSON** to learn how to save and load data from files.  
- Continue using Git to track your progress after each project.

You’ve now enhanced your bank account system with transaction history and list comprehensions, sharpening your Python data handling skills—well done!