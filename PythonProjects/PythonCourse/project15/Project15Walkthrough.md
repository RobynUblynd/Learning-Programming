Below is a detailed walkthrough for Project 15, formatted similarly to `Project10Walkthrough.md`. This guide assumes you’ve been building a bank account system in Python across previous projects, with Project 14 introducing transaction history and list comprehensions. In Project 15, we’ll enhance this system by adding JSON-based data persistence.

---

# Project 15: Working with JSON

In this project, we’ll enhance our bank account system by adding the ability to save and load transaction history using JSON files. This will allow us to persist data between different runs of the program, making our application more practical and user-friendly.

## Objective

- Learn how to use JSON for data serialization and persistence in Python.
- Modify the `BankAccount` class to save and load transaction history to/from a JSON file.
- Understand how to handle file operations and potential errors.

## Task

Enhance the bank account system to:

1. Save the transaction history to a JSON file when the program ends.
2. Load the transaction history from the JSON file when the program starts.
3. Handle cases where the JSON file does not exist or is empty.

## Step-by-Step Guide

### Step 1: Introduction to JSON

JSON (JavaScript Object Notation) is a lightweight data interchange format that’s easy for humans to read and write, and easy for machines to parse and generate. In Python, we can use the built-in `json` module to work with JSON data.

**Why use JSON?**

- It’s human-readable.
- It’s widely used for data exchange between systems.
- It can represent complex data structures like lists and dictionaries.

In this project, we’ll use JSON to save the transaction history of our bank account to a file and load it back when needed.

### Step 2: Modify the BankAccount Class

We’ll add two new methods to the `BankAccount` class in `accounts.py`:

- `save_transactions()`: To save the transaction history to a JSON file.
- `load_transactions()`: To load the transaction history from a JSON file.

Open `accounts.py` in the `project15/` folder (or create it if it doesn’t exist) and update the `BankAccount` class as follows:

```python
import json

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.transactions = []
        self.load_transactions()  # Load transactions when the account is created

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append({"type": "deposit", "amount": amount})
        return f"Deposited ${amount}. Balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append({"type": "withdraw", "amount": amount})
        return f"Withdrew ${amount}. Balance: ${self.balance}"

    def get_total_deposits(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "deposit")

    def get_total_withdrawals(self):
        return sum(t["amount"] for t in self.transactions if t["type"] == "withdraw")

    def show_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
        for t in self.transactions:
            print(f"{t['type'].capitalize()}: ${t['amount']}")

    def save_transactions(self):
        with open("transactions.json", "w") as f:
            json.dump(self.transactions, f)

    def load_transactions(self):
        try:
            with open("transactions.json", "r") as f:
                self.transactions = json.load(f)
                # Recalculate balance based on loaded transactions
                self.balance = sum(t["amount"] for t in self.transactions if t["type"] == "deposit") - \
                               sum(t["amount"] for t in self.transactions if t["type"] == "withdraw")
        except FileNotFoundError:
            self.transactions = []  # If file doesn’t exist, start with an empty list
```

**Explanation:**

- **Imports**: We import the `json` module to handle JSON operations.
- **save_transactions()**: Uses `json.dump()` to write the `transactions` list to "transactions.json".
- **load_transactions()**: Uses `json.load()` to read from "transactions.json". If the file doesn’t exist, it catches the `FileNotFoundError` and initializes `transactions` as an empty list.
- **Balance Recalculation**: After loading, we recalculate `balance` to ensure it matches the transaction history.
- **Existing Methods**: The deposit, withdraw, and analysis methods remain from previous projects but are included for completeness.

**Note**: For simplicity, we’re using "transactions.json" in the same directory as the script. In a real application, you might specify a full file path.

### Step 3: Update the main.py Script

Next, modify `main.py` to load the transaction history at the start and save it after performing transactions.

Open `main.py` in the `project15/` folder and update it as follows:

```python
from accounts import BankAccount

# Create a BankAccount instance (transactions are loaded automatically)
account = BankAccount()

# Display initial balance and transaction history
print(f"Initial Balance: ${account.balance}")
print("Initial Transaction History:")
account.show_transactions()

# Perform some transactions
try:
    print(account.deposit(100))
    print(account.withdraw(30))
    print(account.deposit(50))
    print(account.withdraw(20))
except ValueError as e:
    print(f"Error: {e}")

# Show updated transaction history
print("\nUpdated Transaction History:")
account.show_transactions()

# Show total deposits and withdrawals
print(f"\nTotal Deposits: ${account.get_total_deposits()}")
print(f"Total Withdrawals: ${account.get_total_withdrawals()}")

# Save transactions before exiting
account.save_transactions()
print("Transactions saved to 'transactions.json'.")
```

**Explanation:**

- **Instantiation**: Creating a `BankAccount` instance triggers `load_transactions()` via `__init__`.
- **Initial Display**: Shows the loaded balance and transaction history to verify persistence.
- **Transactions**: Performs sample deposits and withdrawals, wrapped in a try-except block for error handling.
- **Save**: Calls `save_transactions()` to persist the updated history.

### Step 4: Run and Test the Code

Let’s test the new functionality.

**How to Run:**

- In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button.
- Alternatively, in a terminal, navigate to `project15/` and run `python main.py`.

**First Run:**

- Since "transactions.json" doesn’t exist yet, the initial transaction history will be empty.
- The script performs transactions and saves them.

**Second Run:**

- Running the script again loads the transactions from "transactions.json", showing the initial state before adding new transactions.

**Expected Output (First Run):**

```
Initial Balance: $0
Initial Transaction History:
No transactions yet.

Deposited $100. Balance: $100
Withdrew $30. Balance: $70
Deposited $50. Balance: $120
Withdrew $20. Balance: $100

Updated Transaction History:
Deposit: $100
Withdraw: $30
Deposit: $50
Withdraw: $20

Total Deposits: $150
Total Withdrawals: $50
Transactions saved to 'transactions.json'.
```

**Expected Output (Second Run):**

```
Initial Balance: $100
Initial Transaction History:
Deposit: $100
Withdraw: $30
Deposit: $50
Withdraw: $20

Deposited $100. Balance: $200
Withdrew $30. Balance: $170
Deposited $50. Balance: $220
Withdrew $20. Balance: $200

Updated Transaction History:
Deposit: $100
Withdraw: $30
Deposit: $50
Withdraw: $20
Deposit: $100
Withdraw: $30
Deposit: $50
Withdraw: $20

Total Deposits: $300
Total Withdrawals: $100
Transactions saved to 'transactions.json'.
```

**Testing Tip**: Run the script multiple times to confirm that transactions persist and accumulate correctly.

### Step 5: Commit Your Changes Using Git

Save your work with Git to track your progress.

- **Initialize Git (If Not Done):**
  - In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.
  - Or, in a terminal: `git init`.

- **Commit Your Code:**
  - In PyCharm, press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check both `accounts.py` and `main.py`, enter a message like "Completed Project 15: Working with JSON", and click **Commit**.
  - In a terminal:  
    ```bash
    git add accounts.py main.py
    git commit -m "Completed Project 15: Working with JSON"
    ```

**Why**: Committing preserves your work and allows you to track changes over time.

---

## What You’ve Learned

- **JSON Serialization**: Used `json.dump()` and `json.load()` to save and load data.
- **File Handling**: Managed file operations with error handling for missing files.
- **Data Persistence**: Ensured transaction history persists between program runs.
- **Code Organization**: Continued using modules to separate concerns.

---

## Extra Challenges

Want to enhance your project? Try these:

- **Handle Corrupted JSON**: Add try-except blocks to catch `json.JSONDecodeError` for invalid JSON data.
- **Save Multiple Accounts**: Extend the system to save and load data for multiple accounts in a single JSON file.
- **Use a Different File Format**: Experiment with CSV or Python’s `pickle` module instead of JSON.

---

## Next Steps

- Move on to **Project 16: GUI for Bank Account** to learn how to create a graphical user interface.
- Continue using Git to track your progress after each project.

You’ve now added data persistence to your bank account system using JSON, making it more practical and user-friendly—excellent work!