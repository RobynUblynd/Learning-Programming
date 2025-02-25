Welcome to the walkthrough for **Project 8: Basic OOP**! In this project, you’ll dive into the world of **Object-Oriented Programming (OOP)** by building a simple yet powerful **Bank Account** simulator. You’ll learn how to create classes, define methods, and work with objects—core concepts that make Python such a flexible and organized language. By the end, you’ll have a program that lets users deposit, withdraw, check their balance, and quit, all while handling errors like insufficient funds. Let’s get started!

---

## **Objective**
- Understand the basics of **Object-Oriented Programming (OOP)**.
- Learn how to define a **class** and create **objects**.
- Use **methods** to perform actions like depositing and withdrawing money.
- Practice **error handling** to manage common issues, such as insufficient funds.

## **Task**
Create a program that:
1. Defines a `BankAccount` class with methods for depositing, withdrawing, and checking the balance.
2. Uses a loop to allow users to interact with their bank account by choosing actions like deposit, withdraw, check balance, or quit.
3. Handles errors gracefully, such as preventing withdrawals when there are insufficient funds.

---

## **Step-by-Step Guide**

### **Step 1: Create the Project Structure**
Let’s set up your workspace for this project.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: A root folder for all your course projects.  
  - **How**: If it doesn’t exist, in PyCharm, go to **File > New Project**, name it `PythonCourse`, pick a location (e.g., Desktop), and click **Create**.  
  - **Why**: Centralizes all your projects for easy access.

- **Subfolder for Project 8 (`project8/`)**  
  - **What**: A folder just for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click `PythonCourse`, select **New > Directory**, and name it `project8`.  
  - **Why**: Keeps this project separate from others.

- **Python File (`main.py`)**  
  - **What**: The file for your code.  
  - **How**: Right-click `project8/`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a standard name for the main script.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
└── project8/
    └── main.py
```

**Key Takeaway**: A clear structure keeps your work organized and easy to manage.

---

### **Step 2: Write the Code**
Now, let’s build the `BankAccount` class and set up user interaction. Open `main.py` in `project8/` and enter the following code:

```python
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance

# Create an account with an initial balance of $100
account = BankAccount(100)

# Simple interaction loop
while True:
    action = input("Choose action: (D)eposit, (W)ithdraw, (B)alance, (Q)uit: ").upper()
    if action == 'D':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif action == 'W':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif action == 'B':
        print(f"Current balance: ${account.get_balance()}")
    elif action == 'Q':
        print("Thank you for using the bank!")
        break
    else:
        print("Invalid action. Please try again.")
```

Here’s what each part of the code does and why it’s important:

#### **Understanding OOP**
- **Classes and Objects**: A **class** is like a blueprint for creating objects. In this case, `BankAccount` is the class, and `account` is an object (or instance) of that class. Think of the class as a recipe and the object as the cake you bake using that recipe.
- **Attributes**: These are the data stored in an object. Here, `self.balance` is an attribute that holds the current balance of the account.
- **Methods**: These are functions that belong to a class and operate on its attributes. For example, `deposit` and `withdraw` are methods that change the balance.

#### **The `BankAccount` Class**
- **`__init__(self, initial_balance=0)`**: This is the **constructor** method, which runs when you create a new `BankAccount` object. It sets the initial balance (default is 0 if not specified).  
  - **Why**: Initializes the object with starting data.
- **`deposit(self, amount)`**: Adds the specified amount to the balance if it’s positive.  
  - **Why**: Allows users to add money to their account.
- **`withdraw(self, amount)`**: Subtracts the amount from the balance if there are sufficient funds and the amount is positive.  
  - **Why**: Allows users to take money out while preventing overdrafts.
- **`get_balance(self)`**: Returns the current balance.  
  - **Why**: Provides a way to check the account balance without modifying it.

#### **User Interaction Loop**
- **`account = BankAccount(100)`**: Creates a new `BankAccount` object with an initial balance of $100.
- **`while True:`**: Starts an infinite loop for continuous user interaction until the user chooses to quit.
- **`input()` and Conditionals**: Asks the user for an action (D, W, B, Q) and performs the corresponding method:  
  - **D**: Deposit money.  
  - **W**: Withdraw money.  
  - **B**: Check balance.  
  - **Q**: Quit the program.
- **`break`**: Exits the loop when the user chooses to quit.

**Key Takeaway**: OOP helps organize code by bundling data (attributes) and behaviors (methods) into objects, making your programs more modular and easier to understand.

---

### **Step 3: Run the Code**
Let’s test your bank account simulator!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button (top-right).  
  - The program will start, and you’ll see a prompt to choose an action.

- **Sample Interaction**:
  ```
  Choose action: (D)eposit, (W)ithdraw, (B)alance, (Q)uit: B
  Current balance: $100.0

  Choose action: (D)eposit, (W)ithdraw, (B)alance, (Q)uit: D
  Enter amount to deposit: 50
  Deposited $50.0. New balance: $150.0

  Choose action: (D)eposit, (W)ithdraw, (B)alance, (Q)uit: W
  Enter amount to withdraw: 30
  Withdrew $30.0. New balance: $120.0

  Choose action: (D)eposit, (W)ithdraw, (B)alance, (Q)uit: W
  Enter amount to withdraw: 200
  Insufficient funds.

  Choose action: (D)eposit, (W)ithdraw, (B)alance, (Q)uit: Q
  Thank you for using the bank!
  ```

- **Test Different Scenarios**:  
  - Try depositing a negative amount (e.g., -10) to see the error message.  
  - Attempt to withdraw more than the balance to check the "Insufficient funds" message.  
  - Enter an invalid action (e.g., 'X') to see the "Invalid action" message.  

- **Why It’s Important**:  
  - Testing ensures that your methods work as expected and that error handling is in place.  
  - It also helps you understand how the program flows and how objects maintain state (e.g., the balance updates correctly).

**Key Takeaway**: Running and testing your code is crucial for catching mistakes and understanding how OOP works in practice.

---

### **Step 4: Commit Your Changes Using Git**
Save your work to track your progress.

- **Set Up Git (If Needed)**:  
  - **How**: Go to **VCS > Enable Version Control Integration**, pick **Git**, and click **OK**.  
  - **Why**: Tracks changes like a project diary.

- **Commit Your Work**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, type "Completed Project 8: Basic OOP with BankAccount class", and click **Commit**.  
  - **Why**: Saves a milestone you can revisit.

**Key Takeaway**: Git helps you manage your coding journey and keeps your progress safe.

---

## **What You’ve Learned**
- **Object-Oriented Programming (OOP)**: You’ve created a class (`BankAccount`) and used objects to manage data and behavior.  
- **Classes and Objects**: You’ve defined a class and instantiated an object to simulate a bank account.  
- **Methods and Attributes**: You’ve used methods like `deposit` and `withdraw` to interact with the object’s attributes (e.g., `balance`).  
- **Error Handling**: You’ve implemented checks to prevent invalid actions, such as depositing negative amounts or overdrawing the account.  

These concepts are the building blocks of OOP and will be essential as you tackle more complex projects.

---

## **Extra Tips to Boost Your Learning**
- **Add a Transfer Method**: Try creating a `transfer` method that moves money from one account to another. You’ll need to create another `BankAccount` object and handle the transfer logic.  
- **Handle Multiple Accounts**: Modify the program to manage multiple accounts, perhaps using a dictionary to store them by account number.  
- **Experiment with Inheritance**: Create a subclass like `SavingsAccount` that adds interest calculation to the balance.  

**Key Takeaway**: Experimenting with your code reinforces your understanding and sparks creativity.

---

## **Next Steps**
- Start **Project 9: Hangman Game** to apply your OOP skills in a fun, interactive game.  
- Keep committing after each project to track your growth.

---

## **The Big Picture**
You’ve:  
1. Set up `project8/main.py`.  
2. Built a `BankAccount` class with methods for deposits, withdrawals, and balance checks.  
3. Tested your program to ensure it handles different scenarios correctly.  
4. Saved your work with Git.  

**Why It Matters**: You’re not just coding—you’re learning to think like a programmer, organizing your code with OOP principles and building habits that will serve you in more advanced projects. Ready for Project 9? You’ve got this!