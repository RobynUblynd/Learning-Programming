# Project 7: File Handling Walkthrough

In this project, you’ll create an interactive program that handles files to store and process numbers. You’ll allow users to add numbers to a file, display the list of numbers, calculate their sum, and save the result to another file—all while managing potential errors gracefully. This builds on your previous skills and introduces persistent data storage with files.

---

## Objective
- **Learn**: File operations (reading, writing, appending) in Python.
- **Practice**: User interaction, error handling, and modular coding.
- **Build**: A menu-driven program to manage numbers in files.

## Task
Your program will:
1. Store numbers in `numbers.txt`, one per line.
2. Offer a menu with these options:
   - Add a number to the file.
   - Show all numbers in the file.
   - Calculate the sum of the numbers and save it to `sum.txt`.
   - Quit the program.
3. Handle errors like missing files or invalid inputs.

---

## Step-by-Step Guide

### Step 1: Set Up Your Project Structure
A clear project structure keeps your work organized.

- **Main Directory: `PythonCourse`**  
  - **What**: A root folder for all your projects.  
  - **How**: In PyCharm, go to **File > New Project**, name it `PythonCourse`, choose a location (e.g., Desktop), and click **Create**. If it already exists, skip this.  
  - **Why**: Keeps all your projects in one place.

- **Subfolder: `project7`**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer, right-click `PythonCourse`, select **New > Directory**, and name it `project7`.  
  - **Why**: Isolates Project 7 from other work.

- **Python File: `main.py`**  
  - **What**: The script where you’ll write your code.  
  - **How**: Right-click `project7`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: A standard name for the main program file.

**Your Structure**:  
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
└── project7/
    └── main.py
```

---

### Step 2: Write the Code
Open `main.py` in the `project7` folder and add the following code. This program uses functions for modularity and a loop for user interaction.

```python
def add_number():
    try:
        number = float(input("Enter a number: "))
        with open("numbers.txt", "a") as f:
            f.write(f"{number}\n")
        print("Number added.")
    except ValueError:
        print("Invalid number. Please try again.")

def show_numbers():
    try:
        with open("numbers.txt", "r") as f:
            lines = f.readlines()
            numbers = [line.strip() for line in lines if line.strip()]
        if numbers:
            print("Current numbers:")
            for num in numbers:
                print(num)
        else:
            print("No numbers in the file.")
    except FileNotFoundError:
        print("No numbers file found.")

def calculate_sum():
    try:
        with open("numbers.txt", "r") as f:
            lines = f.readlines()
        numbers = []
        for line in lines:
            try:
                numbers.append(float(line.strip()))
            except ValueError:
                pass  # Skip invalid lines
        sum_numbers = sum(numbers)
        with open("sum.txt", "w") as f:
            f.write(f"Sum: {sum_numbers:.2f}\n")
        print(f"Sum calculated: {sum_numbers:.2f}")
    except FileNotFoundError:
        print("No numbers file found. Sum is 0.")

while True:
    print("\nMenu: (A)dd number, (S)how numbers, (C)alculate sum, (Q)uit")
    choice = input("Choose an option: ").strip().upper()
    
    if choice == 'A':
        add_number()
    elif choice == 'S':
        show_numbers()
    elif choice == 'C':
        calculate_sum()
    elif choice == 'Q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

#### Code Breakdown
- **`add_number()`**  
  - **Purpose**: Adds a user-entered number to `numbers.txt`.  
  - **Details**:  
    - Prompts for a number and converts it to a float.  
    - Opens `numbers.txt` in append mode (`"a"`) and writes the number on a new line.  
    - Uses `try-except` to catch invalid inputs (e.g., letters).  
  - **Why**: Enables data input and file appending.

- **`show_numbers()`**  
  - **Purpose**: Displays all entries in `numbers.txt`.  
  - **Details**:  
    - Opens the file in read mode (`"r"`) and reads all lines.  
    - Strips whitespace and skips empty lines.  
    - Handles `FileNotFoundError` if the file doesn’t exist yet.  
  - **Why**: Lets users verify the file’s contents.

- **`calculate_sum()`**  
  - **Purpose**: Computes the sum of numbers and saves it to `sum.txt`.  
  - **Details**:  
    - Reads lines from `numbers.txt`.  
    - Converts each line to a float, skipping invalid entries with a nested `try-except`.  
    - Calculates the sum and writes it to `sum.txt` in write mode (`"w"`), overwriting any previous content.  
    - Handles `FileNotFoundError` for an empty or missing file.  
  - **Why**: Combines reading, processing, and writing.

- **Main Loop**  
  - **Purpose**: Provides a menu-driven interface.  
  - **Details**:  
    - Runs indefinitely until the user quits.  
    - Takes input, converts it to uppercase, and matches it to options (A, S, C, Q).  
    - Calls the appropriate function or exits with `break`.  
  - **Why**: Keeps the program interactive and user-friendly.

#### Key Features
- **File Modes**:  
  - `"r"`: Read existing content.  
  - `"w"`: Write (overwrites the file).  
  - `"a"`: Append (adds to the end).  
- **Context Manager (`with`)**: Automatically closes files after use.  
- **Error Handling**: Prevents crashes from missing files or bad inputs.

---

### Step 3: Run and Test the Program
Let’s see it in action!

- **Running the Code**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or press the green "Play" button.  
  - The program starts in the console.

- **Sample Interaction**:  
  ```
  Menu: (A)dd number, (S)how numbers, (C)alculate sum, (Q)uit
  Choose an option: A
  Enter a number: 5.5
  Number added.

  Menu: (A)dd number, (S)how numbers, (C)alculate sum, (Q)uit
  Choose an option: A
  Enter a number: 10
  Number added.

  Menu: (A)dd number, (S)how numbers, (C)alculate sum, (Q)uit
  Choose an option: S
  Current numbers:
  5.5
  10

  Menu: (A)dd number, (S)how numbers, (C)alculate sum, (Q)uit
  Choose an option: C
  Sum calculated: 15.50

  Menu: (A)dd number, (S)how numbers, (C)alculate sum, (Q)uit
  Choose an option: Q
  Goodbye!
  ```

- **Check the Files**:  
  - Open `numbers.txt` (in `project7/`):  
    ```
    5.5
    10
    ```
  - Open `sum.txt`:  
    ```
    Sum: 15.50
    ```

- **Test Cases**:  
  - **Empty File**: Run `(S)` or `(C)` before adding numbers to see the error messages.  
  - **Invalid Input**: Enter "abc" when adding a number to test `ValueError`.  
  - **Bad File Data**: Manually edit `numbers.txt` to add "hello" and run `(C)`—it skips invalid lines.

---

### Step 4: Save Your Work with Git
Track your progress using version control.

- **Initialize Git (if not already done)**:  
  - Go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.

- **Commit Changes**:  
  - Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac).  
  - Check `main.py`, enter a message like "Completed Project 7: File Handling", and click **Commit**.

- **Why**: Git lets you save snapshots of your work and revert if needed.

---

## What You’ve Learned
- **File Handling**: Reading, writing, and appending to files with different modes.  
- **Error Management**: Using `try-except` to handle file and input errors.  
- **Program Flow**: Building an interactive loop with menu options.  
- **Modularity**: Breaking tasks into functions for cleaner code.

---

## Enhancements to Try
- **Clear File**: Add a `(R)eset` option to erase `numbers.txt` (open in `"w"` mode and write nothing).  
- **Statistics**: Calculate and display the average or count of numbers in `calculate_sum()`.  
- **Custom Files**: Let users specify file names via input.

---

## Next Steps
Move on to **Project 8: Basic OOP**, where you’ll explore classes and objects to organize code further. Keep committing your work to Git after each project!

---

This walkthrough has equipped you with the skills to handle files in Python, a foundational ability for many real-world applications. Great job—now onto the next challenge!