# **Project 2: Simple Calculator**

This guide will help you build a basic calculator in Python, teaching you about variables, data types, and how to perform simple math operations. By the end, you'll understand how to take user input, process it, and display results—key skills for any programmer. We'll maintain a clear structure consistent with previous projects.

---

## **Objective**
- Learn how to use variables to store data.
- Understand different data types, especially numbers (integers and floats).
- Perform basic math operations based on user input using conditionals.

## **Task**
Create a program that:
1. Asks the user for two numbers.
2. Asks for an operation: addition (+), subtraction (-), multiplication (*), or division (/).
3. Performs the chosen operation and displays the result.

---

## **Step-by-Step Guide**

### **Step 1: Create the Project Structure**
Organize your work to keep things tidy—like labeling your school folders.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder for all course projects.  
  - **How**: If it doesn’t exist, in PyCharm, click **File > New Project**, name it `PythonCourse`, choose a location (e.g., Desktop), and hit **Create**.  
  - **Why**: Centralizes all projects, like a binder for your assignments.

- **Subfolder for Project 2 (`project2/`)**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click `PythonCourse`, choose **New > Directory**, and name it `project2`.  
  - **Why**: Keeps projects separate to avoid confusion.

- **Python File (`main.py`)**  
  - **What**: The file where your code will live.  
  - **How**: Right-click `project2/`, select **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a standard name for the main script—like the title page of your project.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
└── project2/
    └── main.py
```

**Key Takeaway**: Good organization saves time and prevents mix-ups as projects grow.

---

### **Step 2: Write the Code**
Now, let’s build the calculator! Open `main.py` in `project2/` and type the following code:

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2

print(f"Result: {result}")
```

Here’s what each part does and why it matters:

- **Line 1: `num1 = float(input("Enter first number: "))`**  
  - **What**: Prompts "Enter first number: ", takes input (e.g., "10.5"), converts it to a float, and stores it in `num1`.  
  - **How**: `input()` gets text; `float()` converts it to a decimal number.  
  - **Why**: Allows decimal inputs. Variables like `num1` store data—like labeled boxes.

- **Line 2: `num2 = float(input("Enter second number: "))`**  
  - **What**: Same as above, but for the second number, stored in `num2`.  
  - **Why**: You need two numbers for math operations.

- **Line 3: `op = input("Enter operation (+, -, *, /): ")`**  
  - **What**: Prompts "Enter operation (+, -, *, /): ", takes input (e.g., "+"), and stores it in `op`.  
  - **How**: `input()` gets text; no conversion needed since operations are strings.  
  - **Why**: Makes the program interactive by letting the user choose.

- **Lines 5-12: Conditionals (`if`, `elif`)**
  - **What**: Checks `op` and calculates:  
    - `+` adds, `-` subtracts, `*` multiplies, `/` divides.  
  - **How**: `if` and `elif` test conditions; `==` checks equality.  
  - **Why**: Enables decision-making based on user input.

- **Line 14: `print(f"Result: {result}")`**  
  - **What**: Displays the result (e.g., "Result: 15.0") using an f-string.  
  - **Why**: Shows the outcome, completing the program’s purpose.

**Key Concepts**:
- **Variables**: Store data (e.g., `num1`, `result`).  
- **Data Types**: Floats for numbers, strings for `op`.  
- **Conditionals**: Control program flow.

**Key Takeaway**: This code teaches input handling, calculations, and decision-making—core programming skills.

---

### **Step 3: Run the Code**
Test your calculator to ensure it works!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button (top-right).  
  - In the console:  
    ```
    Enter first number: 10
    Enter second number: 5
    Enter operation (+, -, *, /): +
    Result: 15.0
    ```

- **Test Different Inputs**:  
  - Decimals (e.g., `3.5 * 2.0` → `Result: 7.0`).  
  - Division (e.g., `10 / 2` → `Result: 5.0`).  

- **Why It’s Important**:  
  - Confirms the code works and helps you understand Python’s flow.

**Key Takeaway**: Testing verifies functionality and builds confidence.

---

### **Step 4: Commit Your Changes Using Git**
Save your work to track progress.

- **Ensure Git Is Set Up**:  
  - **How**: If not initialized, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Tracks changes like a history log.

- **Commit**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, write "Completed Project 2: Simple Calculator", and click **Commit**.  
  - **Why**: Saves a snapshot to revert to if needed.

**Key Takeaway**: Committing preserves your progress.

---

## **What You’ve Learned**
- Variables for data storage.
- Data types (floats, strings).
- Math operations and conditionals.
- User input handling.

These build on prior projects and prepare you for more complexity.

---

## **Extra Tips to Boost Your Learning**
- **Add Operations**: Try exponentiation (`**`) or modulus (`%`).  
- **Error Handling**: Add an `else` for invalid operations (e.g., `print("Invalid operation")`).  
- **Experiment**: Use `int()` instead of `float()`—see what changes.

---

## **Next Steps**
- Begin **Project 3: Number Guessing Game** for loops and conditionals.  
- Keep committing after each project.

---

## **The Big Picture**
You’ve:
1. Organized `project2/main.py`.  
2. Coded a calculator.  
3. Tested it.  
4. Saved it with Git.

**Why It Matters**: You’re building programming habits and skills for future success. Ready for the next challenge!

--- 

This walkthrough is now streamlined without the environment setup step, ensuring clarity and focus on the project itself.