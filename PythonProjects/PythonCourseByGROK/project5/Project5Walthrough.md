# **Project 5: Simple To-Do List**

In this project, you’ll build a simple to-do list manager in Python. You’ll learn how to use **lists** to store tasks and **functions** to organize your code. By the end, you’ll have a program that allows users to add tasks, display the task list, and quit the program.

---

## **Objective**
- Learn how to use lists to store and manage data.
- Practice defining and calling functions to perform specific tasks.
- Understand how to use loops for repeated user interactions.

## **Task**
Create a program that:
1. Uses a list to store tasks.
2. Defines two functions:
   - `add_task(tasks, task)`: Adds a new task to the list.
   - `show_tasks(tasks)`: Displays all tasks in the list.
3. Provides a simple menu for the user to add tasks, show tasks, or quit the program.

---

## **Step-by-Step Guide**

### **Step 1: Create the Project Structure**
Organize your work to keep things tidy—like sorting your notes into folders.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: A root folder for all your course projects.  
  - **How**: If it doesn’t exist, in PyCharm, go to **File > New Project**, name it `PythonCourse`, pick a location (e.g., Desktop), and click **Create**.  
  - **なぜ**: Centralizes all projects for easy access.

- **Subfolder for Project 5 (`project5/`)**  
  - **What**: A folder just for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click `PythonCourse`, select **New > Directory**, and name it `project5`.  
  - **Why**: Keeps this project separate from others.

- **Python File (`main.py`)**  
  - **What**: The file for your code.  
  - **How**: Right-click `project5/`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a standard name for the main script.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── project3/
│   └── main.py
├── project4/
│   └── main.py
└── project5/
    └── main.py
```

**Key Takeaway**: A clear structure saves time and avoids confusion.

---

### **Step 2: Write the Code**
Let’s build the to-do list manager! Open `main.py` in `project5/` and enter this code:

```python
def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def show_tasks(tasks):
    if tasks:
        print("Your to-do list:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

tasks = []

while True:
    print("\nMenu: (A)dd task, (S)how tasks, (Q)uit")
    choice = input("Choose an option: ").strip().upper()
    
    if choice == 'A':
        task = input("Enter the task: ")
        add_task(tasks, task)
    elif choice == 'S':
        show_tasks(tasks)
    elif choice == 'Q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

Here’s what each part does and why it’s important:

- **Function: `add_task(tasks, task)`**  
  - **What**: Adds a new task to the `tasks` list using `append()`.  
  - **Why**: Keeps the code organized by separating the task-adding logic into its own function.

- **Function: `show_tasks(tasks)`**  
  - **What**: Displays all tasks in the list, numbered for clarity. If the list is empty, it informs the user.  
  - **How**: Uses `enumerate()` to number tasks automatically.  
  - **Why**: Makes it easy to see the current tasks and improves user experience.

- **`tasks = []`**  
  - **What**: Initializes an empty list to store tasks.  
  - **Why**: Lists are perfect for storing multiple items, like tasks, in order.

- **`while True:`**  
  - **What**: Starts an infinite loop to keep the program running until the user chooses to quit.  
  - **Why**: Allows the user to perform multiple actions without restarting the program.

- **Menu and User Input**  
  - **What**: Displays a menu and asks the user to choose an option (A, S, or Q).  
  - **How**: Uses `input()` and converts the choice to uppercase for consistency.  
  - **Why**: Provides a simple interface for user interaction.

- **Conditionals (`if`, `elif`, `else`)**  
  - **What**: Decides what to do based on the user’s choice:  
    - 'A': Add a task.  
    - 'S': Show tasks.  
    - 'Q': Quit the program.  
    - Else: Handle invalid input.  
  - **Why**: Controls the program flow based on user decisions.

**Key Concepts**:
- **Lists**: Store multiple items in order.  
- **Functions**: Organize code into reusable blocks.  
- **Loops**: Repeat actions until a condition is met.  
- **User Input**: Interact with the user through `input()`.

**Key Takeaway**: Lists and functions make your code more flexible and easier to manage.

---

### **Step 3: Run the Code**
Test your to-do list manager to ensure it works!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or hit the green "Play" button (top-right).  
  - Example interaction:  
    ```
    Menu: (A)dd task, (S)how tasks, (Q)uit
    Choose an option: A
    Enter the task: Buy groceries
    Task 'Buy groceries' added.
    
    Menu: (A)dd task, (S)how tasks, (Q)uit
    Choose an option: S
    Your to-do list:
    1. Buy groceries
    
    Menu: (A)dd task, (S)how tasks, (Q)uit
    Choose an option: Q
    Goodbye!
    ```

- **Test Different Scenarios**:  
  - Add multiple tasks and display them.  
  - Try showing tasks when the list is empty.  
  - Enter an invalid option to see the error message.  

- **Why Test**:  
  - Confirms that the list stores tasks correctly.  
  - Ensures the menu and functions work as expected.

**Key Takeaway**: Testing helps you understand how your code behaves in different situations.

---

### **Step 4: Commit Your Changes Using Git**
Save your work with Git to track progress.

- **Set Up Git (If Needed)**:  
  - **How**: Go to **VCS > Enable Version Control Integration**, pick **Git**, and click **OK**.  
  - **Why**: Tracks changes like a project diary.

- **Commit Your Work**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, type "Completed Project 5: Simple To-Do List with lists and functions", and click **Commit**.  
  - **Why**: Saves a milestone you can revisit.

**Key Takeaway**: Git helps you manage your coding journey.

---

## **What You’ve Learned**
- **Lists**: Store and manage multiple items.  
- **Functions**: Organize code into reusable parts.  
- **Loops**: Keep the program running for multiple interactions.  
- **User Input and Menus**: Create interactive programs.  

These skills build on past projects and prepare you for more complex tasks.

---

## **Extra Tips**
- **Remove Tasks**: Add a function to remove tasks by number.  
- **Save to File**: Try saving the task list to a file for persistence.  
- **Experiment**: Add task priorities or due dates for a challenge.

**Key Takeaway**: Tweaking your code boosts creativity and understanding.

---

## **Next Steps**
- Start **Project 6: Student Grades** to practice dictionaries.  
- Keep committing after each project to track your growth.

---

## **The Big Picture**
You’ve:  
1. Set up `project5/main.py`.  
2. Built a to-do list manager using lists and functions.  
3. Tested it for functionality.  
4. Saved it with Git.

**Why It Matters**: You’re mastering Python’s core concepts, thinking like a programmer, and developing good habits. Ready for Project 6? Let’s keep going!