Below is a detailed walkthrough for **Project 19**, formatted consistently with the style of `Project10Walkthrough.md`. This guide will walk you through creating a Python program that uses **regular expressions** to validate and extract information from user input, such as email addresses. By the end, you’ll have a working program that demonstrates the power of regular expressions for pattern matching and data validation.

---

## Objective
- Understand the basics of **regular expressions** in Python.
- Learn to use the `re` module for pattern matching and validation.
- Practice creating and applying regular expressions to validate common data formats like email addresses.

## Task
Create a program that:
1. Asks the user to input an email address.
2. Uses a regular expression to validate whether the input is a properly formatted email address.
3. Provides feedback to the user indicating whether the email is valid or not.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Set up an organized workspace for your code.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder containing all your course projects.  
  - **How**: If it doesn’t exist, open PyCharm, go to **File > New Project**, name it `PythonCourse`, select a location (e.g., Desktop), and click **Create**. If it already exists, open it via **File > Open** and select `PythonCourse`.  
  - **Why**: Centralizes all your projects for easy management.

- **Subfolder for Project 19 (`project19/`)**  
  - **What**: A dedicated folder for this project’s files.  
  - **How**: In PyCharm’s Project Explorer, right-click `PythonCourse`, select **New > Directory**, and name it `project19`.  
  - **Why**: Isolates Project 19’s files to maintain clarity.

- **Python File (`main.py`)**  
  - **What**: The script where you’ll write your code.  
  - **How**: Right-click `project19/`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a conventional name for the primary script.

**Expected Structure**:
```
PythonCourse/
├── project1/
│   └── main.py
├── ...
├── project18/
│   └── main.py
└── project19/
    └── main.py
```

---

### Step 2: Import the `re` Module
To use regular expressions, you need to import Python’s `re` module.

- **What**: Add an import statement for the `re` module at the top of `main.py`.  
- **How**: Open `main.py` in the `project19/` folder and add:
  ```python
  import re
  ```
- **Why**:  
  - **Regular Expressions**: The `re` module provides functions to work with regular expressions, which are powerful tools for pattern matching and text manipulation.

---

### Step 3: Define the Email Validation Function
Create a function that uses a regular expression to check if a given string is a valid email address.

- **What**: A function `is_valid_email` that takes a string and returns `True` if it matches the email pattern, otherwise `False`.  
- **How**: Add this code below the import statement:
  ```python
  def is_valid_email(email):
      pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
      return bool(re.match(pattern, email))
  ```
- **Why**:  
  - **Pattern Explanation**:  
    - `^`: Start of the string.  
    - `[a-zA-Z0-9_.+-]+`: One or more alphanumeric characters, underscores, dots, pluses, or hyphens (for the local part before the `@`).  
    - `@`: The `@` symbol.  
    - `[a-zA-Z0-9-]+`: One or more alphanumeric characters or hyphens (for the domain name).  
    - `\.`: A literal dot.  
    - `[a-zA-Z0-9-.]+`: One or more alphanumeric characters, dots, or hyphens (for the top-level domain).  
    - `$`: End of the string.  
  - **re.match**: Checks if the pattern matches the beginning of the string.  
  - **bool()**: Converts the match object to `True` if there’s a match, otherwise `False`.

**Note**: This pattern is a simplified email validator and may not cover all edge cases defined by the official email specification (RFC 5322), but it works well for most common email formats.

---

### Step 4: Get User Input and Validate
Prompt the user to enter an email address and use the validation function to check it.

- **What**: Add code to get user input and validate it using `is_valid_email`.  
- **How**: Append this code to `main.py`:
  ```python
  # Get user input
  email = input("Enter an email address: ")

  # Validate and provide feedback
  if is_valid_email(email):
      print("Valid email address!")
  else:
      print("Invalid email address!")
  ```
- **Why**:  
  - **User Interaction**: Allows the user to input an email address.  
  - **Validation**: Uses the `is_valid_email` function to check the input and provides immediate feedback.

---

### Step 5: Run and Test the Code
Ensure your program works correctly by testing it with various inputs.

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or press the green "Play" button.  
  - The program will prompt you to enter an email address in the console.

- **Test Cases**:  
  - **Valid Email**:  
    - Input: `user@example.com`  
    - Expected Output: `Valid email address!`  
  - **Invalid Email (missing @)**:  
    - Input: `userexample.com`  
    - Expected Output: `Invalid email address!`  
  - **Invalid Email (missing domain)**:  
    - Input: `user@.com`  
    - Expected Output: `Invalid email address!`  
  - **Valid Email with Subdomain**:  
    - Input: `user@mail.example.com`  
    - Expected Output: `Valid email address!`  
  - **Invalid Email (special characters)**:  
    - Input: `user!name@example.com`  
    - Expected Output: `Invalid email address!` (since `!` is not allowed in this pattern)

- **Why Test**: Verifies that the regular expression correctly identifies valid and invalid email formats.

---

### Step 6: Commit Your Work with Git
Use version control to save your progress.

- **Enable Git (If Needed)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Initializes Git for your project if it’s not already set up.

- **Commit Changes**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, enter a commit message like "Completed Project 19: Regular Expressions for Email Validation", and click **Commit**.  
  - **Why**: Records your work in a version-controlled snapshot.

---

## Complete Code for `main.py`
Here’s the full code for your reference:

```python
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

# Get user input
email = input("Enter an email address: ")

# Validate and provide feedback
if is_valid_email(email):
    print("Valid email address!")
else:
    print("Invalid email address!")
```

---

## What You’ve Learned
- **Regular Expressions**: Used the `re` module to define and apply a pattern for email validation.  
- **Pattern Matching**: Constructed a regex pattern to match common email address formats.  
- **Validation Logic**: Implemented a function to validate user input and provide feedback.

---

## Extra Challenges
Take your skills further with these optional exercises:  
- **Extract Domain**: Modify the program to extract and display the domain part of a valid email (e.g., `example.com` from `user@example.com`).  
- **Validate Phone Numbers**: Create a similar function to validate phone numbers using a different regex pattern (e.g., `(123) 456-7890` or `123-456-7890`).  
- **Improve Email Pattern**: Research and implement a more comprehensive email validation pattern that handles additional cases (e.g., quoted local parts or IP addresses in brackets).

---

## Next Steps
- Move on to **Project 20: Contact Book Application** to combine multiple concepts into a capstone project.  
- Keep using Git to track your progress in subsequent projects.

Congratulations! You’ve completed Project 19 and gained practical experience with regular expressions in Python!