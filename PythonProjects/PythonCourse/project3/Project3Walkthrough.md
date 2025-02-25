# **Project 3: Number Guessing Game**

This guide will walk you through creating a fun number guessing game in Python. You’ll learn how to use **loops** and **conditionals**—key tools for controlling program flow and making decisions. By the end, you’ll have a working game where the computer picks a random number, and the user guesses it with hints like "Too high" or "Too low." Let’s dive in!

---

## **Objective**
- Learn about control structures: **loops** and **conditionals**.
- Build skills in user interaction and program flow.

## **Task**
Create a program that:
1. Generates a random number between 1 and 100.
2. Asks the user to guess the number.
3. Gives hints ("Too high" or "Too low") until the user guesses correctly.
4. Congratulates the user when they succeed.

---

## **Step-by-Step Guide**

### **Step 1: Create the Project Structure**
Keep your work organized—like labeling folders for school.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: A root folder for all your course projects.  
  - **How**: If it doesn’t exist, in PyCharm, go to **File > New Project**, name it `PythonCourse`, pick a location (e.g., Desktop), and click **Create**.  
  - **Why**: Keeps all projects in one place, like a binder.

- **Subfolder for Project 3 (`project3/`)**  
  - **What**: A folder just for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click `PythonCourse`, select **New > Directory**, and name it `project3`.  
  - **Why**: Separates this project from others to avoid mix-ups.

- **Python File (`main.py`)**  
  - **What**: The file for your code.  
  - **How**: Right-click `project3/`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a common name for the main script—like a project’s title page.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
└── project3/
    └── main.py
```

**Key Takeaway**: Good organization saves time and keeps things clear.

---

### **Step 2: Write the Code**
Let’s code the game! Open `main.py` in `project3/` and enter this:

```python
import random

number = random.randint(1, 100)
guess = 0

while guess != number:
    guess = int(input("Guess a number (1-100): "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("Congratulations, you guessed it!")
```

Here’s what each part does and why it’s important:

- **`import random`**  
  - **What**: Imports Python’s random module.  
  - **Why**: Lets the program generate a random number, making the game unpredictable.

- **`number = random.randint(1, 100)`**  
  - **What**: Picks a random integer from 1 to 100 and stores it in `number`.  
  - **Why**: This is the secret number the user must guess—like a hidden target.

- **`guess = 0`**  
  - **What**: Sets `guess` to 0 to start the loop.  
  - **Why**: Ensures the loop runs initially, since 0 isn’t a valid guess (1-100).

- **`while guess != number:`**  
  - **What**: Starts a loop that repeats until the guess matches the number.  
  - **How**: The `while` loop runs its indented code as long as `guess` isn’t `number`.  
  - **Why**: Loops let the program keep asking for guesses—perfect for games.

- **`guess = int(input("Guess a number (1-100): "))`**  
  - **What**: Asks the user for a guess, converts it to an integer, and updates `guess`.  
  - **How**: `input()` gets text; `int()` makes it a number.  
  - **Why**: Numbers are needed for comparisons; this connects the user to the game.

- **`if guess < number:`**  
  - **What**: Checks if the guess is less than the number and prints "Too low!"  
  - **Why**: Guides the user to guess higher.

- **`elif guess > number:`**  
  - **What**: Checks if the guess is more than the number and prints "Too high!"  
  - **Why**: Helps the user adjust downward.

- **`print("Congratulations, you guessed it!")`**  
  - **What**: Shows a win message when the loop ends (guess equals number).  
  - **Why**: Celebrates the user’s success, ending the game.

**Key Concepts**:
- **Loops**: Repeat actions with `while`.  
- **Conditionals**: Decide what to do with `if` and `elif`.  
- **Randomness**: Add variety with `random.randint()`.

**Key Takeaway**: You’re learning to control a program’s flow—vital for interactive coding.

---

### **Step 3: Run the Code**
Test your game to see it in action!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or hit the green "Play" button (top-right).  
  - The console shows:  
    ```
    Guess a number (1-100): 
    ```
  - Type a number (e.g., `50`). You might see:  
    ```
    Too high!
    Guess a number (1-100): 
    ```
  - Keep guessing until:  
    ```
    Congratulations, you guessed it!
    ```

- **Test It Out**:  
  - Guess high, low, and correctly to check the hints.  
  - Try a letter (e.g., "abc")—it may crash (we’ll fix this later).

- **Why Test**:  
  - Confirms loops and conditionals work.  
  - Shows the program’s flow in real-time.

**Key Takeaway**: Running and testing help you see your code come to life.

---

### **Step 4: Commit Your Changes Using Git**
Save your work with Git to track progress.

- **Set Up Git (If Needed)**:  
  - **How**: Go to **VCS > Enable Version Control Integration**, pick **Git**, and click **OK**.  
  - **Why**: Tracks changes like a project diary.

- **Commit Your Work**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, type "Completed Project 3: Number Guessing Game", and click **Commit**.  
  - **Why**: Saves a milestone you can revisit.

**Key Takeaway**: Git helps you manage your coding journey.

---

## **What You’ve Learned**
- **Loops**: Repeat tasks with `while` until a goal is reached.  
- **Conditionals**: Make choices with `if` and `elif`.  
- **Random Numbers**: Create variety with `random.randint()`.  
- **User Input**: Engage users with `input()` and feedback.

These build on past projects and set you up for more!

---

## **Extra Tips**
- **Guess Limit**: Add a counter to limit guesses (e.g., 10 tries).  
- **Difficulty**: Offer ranges like 1-50 (easy) or 1-100 (hard).  
- **Experiment**: Try new hints or ranges to customize the game.

**Key Takeaway**: Tweaking your code boosts creativity and understanding.

---

## **Next Steps**
- Start **Project 4: Temperature Converter** to explore functions.  
- Keep committing after each project to track your growth.

---

## **The Big Picture**
You’ve:  
1. Set up `project3/main.py`.  
2. Built a guessing game with loops and conditionals.  
3. Tested it for fun and learning.  
4. Saved it with Git.

**Why It Matters**: You’re not just coding—you’re thinking like a programmer, mastering Python step by step. Ready for Project 4? Let’s go!