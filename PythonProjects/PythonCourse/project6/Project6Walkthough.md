# **Project 6: Student Grades Walkthrough**

Welcome to the walkthrough for **Project 6: Student Grades**! In this project, you’ll create a Python program to manage student grades using **dictionaries** and **functions**. By the end, you’ll have a functional program that lets users add students, update grades, display all grades, and quit—perfect for mastering data structures and user interaction. Let’s dive in step by step!

---

## **Objective**
- Use **dictionaries** to store student names (keys) and their grades (values).
- Define **functions** to handle specific tasks like adding or updating grades.
- Implement a **menu-driven loop** for user interaction.

## **What You’ll Build**
A program that:
1. Stores student names and grades in a dictionary.
2. Offers functions to:
   - Add a new student with a grade.
   - Update an existing student’s grade.
   - Display all students and their grades.
3. Provides a menu with options: Add, Update, Show grades, or Quit.

---

## **Step-by-Step Guide**

### **Step 1: Set Up Your Project**
Let’s organize your workspace for clarity.

- **Create the Main Directory**  
  - **What**: A folder called `PythonCourse` for all your projects.  
  - **How**: In PyCharm, go to **File > New Project**, name it `PythonCourse`, choose a location (e.g., Desktop), and click **Create**. If it already exists, skip this.  
  - **Why**: Keeps all your projects in one place.

- **Add a Subfolder for Project 6**  
  - **What**: A folder named `project6` inside `PythonCourse`.  
  - **How**: In PyCharm’s Project Explorer, right-click `PythonCourse`, select **New > Directory**, and name it `project6`.  
  - **Why**: Isolates this project’s files.

- **Create the Python File**  
  - **What**: A file called `main.py` for your code.  
  - **How**: Right-click `project6`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: It’s where your program lives.

**Your File Structure**:
```
PythonCourse/
├── project6/
│   └── main.py
```

---

### **Step 2: Write the Code**
Open `main.py` in `project6/` and add the following code. This creates a fully functional student grades manager.

```python
def add_student(grades, name, grade):
    if name not in grades:
        grades[name] = grade
        print(f"Student '{name}' added with grade {grade}.")
    else:
        print(f"Student '{name}' already exists. Use update to change the grade.")

def update_grade(grades, name, grade):
    if name in grades:
        grades[name] = grade
        print(f"Grade for '{name}' updated to {grade}.")
    else:
        print(f"Student '{name}' not found. Use add to insert a new student.")

def show_grades(grades):
    if grades:
        print("Student Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students in the record.")

grades = {}

while True:
    print("\nMenu: (A)dd student, (U)pdate grade, (S)how grades, (Q)uit")
    choice = input("Choose an option: ").strip().upper()
    
    if choice == 'A':
        name = input("Enter student name: ")
        grade = float(input("Enter grade: "))
        add_student(grades, name, grade)
    elif choice == 'U':
        name = input("Enter student name: ")
        grade = float(input("Enter new grade: "))
        update_grade(grades, name, grade)
    elif choice == 'S':
        show_grades(grades)
    elif choice == 'Q':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

#### **Code Breakdown**
- **`add_student(grades, name, grade)`**  
  - Checks if the student isn’t already in the dictionary. If not, adds them with their grade. Otherwise, prompts to use the update function.
  - **Why**: Prevents overwriting existing data.

- **`update_grade(grades, name, grade)`**  
  - Updates the grade if the student exists; otherwise, suggests adding them first.  
  - **Why**: Keeps updates intentional and safe.

- **`show_grades(grades)`**  
  - Displays all students and grades if the dictionary isn’t empty; otherwise, shows a “no students” message.  
  - Uses `items()` to loop through key-value pairs.  
  - **Why**: Gives a clear snapshot of the data.

- **`grades = {}`**  
  - Initializes an empty dictionary to hold student-grade pairs.  
  - **Why**: Dictionaries are perfect for quick lookups by name.

- **`while True:` Loop**  
  - Runs the program indefinitely until the user quits with 'Q'.  
  - **Why**: Enables multiple operations in one session.

- **Menu Logic**  
  - Displays options (A, U, S, Q) and processes the user’s choice (case-insensitive thanks to `.upper()`).  
  - **Why**: Makes the program interactive and user-friendly.

---

### **Step 3: Run and Test the Program**
Let’s see it in action!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button.

- **Sample Interaction**:
```
Menu: (A)dd student, (U)pdate grade, (S)how grades, (Q)uit
Choose an option: A
Enter student name: Alice
Enter grade: 85
Student 'Alice' added with grade 85.0.

Menu: (A)dd student, (U)pdate grade, (S)how grades, (Q)uit
Choose an option: S
Student Grades:
Alice: 85.0

Menu: (A)dd student, (U)pdate grade, (S)how grades, (Q)uit
Choose an option: U
Enter student name: Alice
Enter new grade: 90
Grade for 'Alice' updated to 90.0.

Menu: (A)dd student, (U)pdate grade, (S)how grades, (Q)uit
Choose an option: Q
Goodbye!
```

- **Test Cases**:  
  - Add multiple students (e.g., Bob with 92, Charlie with 78) and use 'S' to display them.  
  - Try updating a non-existent student (e.g., Dave) to see the error message.  
  - Choose 'S' with an empty dictionary to check the “no students” message.  
  - Enter an invalid option (e.g., 'X') to test error handling.

- **Why Test**: Ensures every function works and handles edge cases correctly.

---

### **Step 4: Save Your Work (Optional with Git)**
If you’re using version control, save your progress.

- **Enable Git**:  
  - Go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.

- **Commit Changes**:  
  - Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, enter a message like "Completed Project 6: Student Grades", and click **Commit**.  
  - **Why**: Tracks your work like a project log.

---

## **Key Concepts Learned**
- **Dictionaries**: Efficiently store and access key-value pairs (student names and grades).  
- **Functions**: Break code into reusable, task-specific blocks.  
- **Loops**: Enable continuous user interaction with `while True`.  
- **User Input**: Use `input()` to make the program interactive.

---

## **Enhancement Ideas**
- **Delete Option**: Add a function to remove students (e.g., `del grades[name]`).  
- **Grade Average**: Calculate and display the average grade with `sum(grades.values()) / len(grades)`.  
- **More Data**: Store multiple grades per student using lists (e.g., `grades[name] = [85, 90]`).

---

## **Next Steps**
- Move on to **Project 7: File Handling** to learn how to save your grades to a file.  
- Keep practicing with dictionaries and functions—they’re Python essentials!

---

## **Summary**
You’ve built a student grades manager in `project6/main.py` using dictionaries, functions, and a menu-driven loop. You’ve tested it thoroughly and (optionally) saved it with Git. Great job—you’re leveling up your Python skills! Ready for the next challenge? Let’s keep the momentum going!