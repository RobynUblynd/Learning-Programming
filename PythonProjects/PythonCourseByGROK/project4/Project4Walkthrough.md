# **Project 4: Temperature Converter**

In this project, you’ll build a temperature converter in Python. You’ll learn how to use **functions**—a crucial concept for organizing and reusing code. By the end, you’ll have a program that asks the user for a temperature and conversion direction, then displays the result.

---

## **Objective**
- Learn how to define and use functions.
- Practice handling user input and making decisions with conditionals.

## **Task**
Create a program that:
1. Defines two functions:
   - `c_to_f(celsius)`: Converts Celsius to Fahrenheit.
   - `f_to_c(fahrenheit)`: Converts Fahrenheit to Celsius.
2. Asks the user for the conversion direction (C to F or F to C).
3. Asks for the temperature value.
4. Calls the appropriate function and displays the converted temperature.

---

## **Step-by-Step Guide**

### **Step 1: Create the Project Structure**
Keep your work organized—like sorting your notes into folders.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: A root folder for all your course projects.  
  - **How**: If it doesn’t exist, in PyCharm, go to **File > New Project**, name it `PythonCourse`, pick a location (e.g., Desktop), and click **Create**.  
  - **Why**: Centralizes all projects for easy access.

- **Subfolder for Project 4 (`project4/`)**  
  - **What**: A folder just for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click `PythonCourse`, select **New > Directory**, and name it `project4`.  
  - **Why**: Keeps this project separate from others.

- **Python File (`main.py`)**  
  - **What**: The file for your code.  
  - **How**: Right-click `project4/`, choose **New > Python File**, and name it `main.py`.  
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
└── project4/
    └── main.py
```

**Key Takeaway**: A clear structure saves time and avoids confusion.

---

### **Step 2: Write the Code**
Let’s build the converter! Open `main.py` in `project4/` and enter this code:

```python
def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ").strip().upper()

if choice == 'C':
    temp = float(input("Enter temperature in Celsius: "))
    result = c_to_f(temp)
    print(f"{temp}°C is {result}°F")
elif choice == 'F':
    temp = float(input("Enter temperature in Fahrenheit: "))
    result = f_to_c(temp)
    print(f"{temp}°F is {result}°C")
else:
    print("Invalid choice. Please enter C or F.")
```

Here’s what each part does and why it’s important:

- **Functions (`def c_to_f` and `def f_to_c`)**  
  - **What**: Define conversions:
    - `c_to_f(celsius)`: Takes Celsius and returns Fahrenheit.
    - `f_to_c(fahrenheit)`: Takes Fahrenheit and returns Celsius.
  - **How**: Use formulas:  
    - Celsius to Fahrenheit: `(celsius * 9/5) + 32`  
    - Fahrenheit to Celsius: `(fahrenheit - 32) * 5/9`  
  - **Why**: Functions organize code, making it reusable and easier to read.

- **`choice = input(...)`**  
  - **What**: Asks for conversion direction (C or F).  
  - **How**: `.strip().upper()` ensures the input is clean and uppercase (e.g., 'c' becomes 'C').  
  - **Why**: Makes the program flexible and user-friendly.

- **Conditionals (`if`, `elif`, `else`)**  
  - **What**: Decides which conversion to perform based on `choice`.  
  - **How**:  
    - If 'C', asks for Celsius, calls `c_to_f`, and prints the result.  
    - If 'F', asks for Fahrenheit, calls `f_to_c`, and prints the result.  
    - Else, shows an error message.  
  - **Why**: Guides the program based on user input.

- **`temp = float(input(...))`**  
  - **What**: Gets the temperature as a float (allows decimals).  
  - **Why**: Temperatures can be decimals (e.g., 36.6°C).

- **`print(f"{temp}°C is {result}°F")`**  
  - **What**: Displays the result using an f-string for clean formatting.  
  - **Why**: Provides clear, readable output.

**Key Concepts**:
- **Functions**: Mini-programs that perform specific tasks.  
- **Parameters**: Inputs to functions (e.g., `celsius`).  
- **Return Values**: Outputs from functions (e.g., Fahrenheit).  
- **Conditionals**: Make decisions based on conditions.

**Key Takeaway**: Functions help structure code, making it modular and easier to manage.

---

### **Step 3: Run the Code**
Test your converter to ensure it works!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or hit the green "Play" button (top-right).  
  - Example interaction:  
    ```
    Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): C
    Enter temperature in Celsius: 0
    0.0°C is 32.0°F
    ```

- **Test Different Inputs**:  
  - Convert 100°C to Fahrenheit (212°F).  
  - Convert 32°F to Celsius (0°C).  
  - Enter an invalid choice (e.g., 'X') to see the error message.  

- **Why Test**:  
  - Confirms functions and conditionals work.  
  - Ensures the program handles inputs correctly.

**Key Takeaway**: Testing verifies your code and deepens your understanding.

---

### **Step 4: Commit Your Changes Using Git**
Save your work with Git to track progress.

- **Set Up Git (If Needed)**:  
  - **How**: Go to **VCS > Enable Version Control Integration**, pick **Git**, and click **OK**.  
  - **Why**: Tracks changes like a project diary.

- **Commit Your Work**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, type "Completed Project 4: Temperature Converter with functions", and click **Commit**.  
  - **Why**: Saves a milestone you can revisit.

**Key Takeaway**: Git helps you manage your coding journey.

---

## **What You’ve Learned**
- **Functions**: Define and call them to organize code.  
- **Parameters and Return Values**: Pass data to functions and get results.  
- **User Input**: Handle choices and values with `input()`.  
- **Conditionals**: Control program flow based on conditions.  

These skills build on past projects and prepare you for more complex tasks.

---

## **Extra Tips**
- **Multiple Conversions**: Add a loop to allow repeated conversions without restarting.  
- **Error Handling**: Handle non-numeric inputs (e.g., letters) gracefully.  
- **Experiment**: Add Kelvin conversions for a challenge.

**Key Takeaway**: Tweaking your code boosts creativity and understanding.

---

## **Next Steps**
- Start **Project 5: Simple To-Do List** to practice lists and functions.  
- Keep committing after each project to track your growth.

---

## **The Big Picture**
You’ve:  
1. Set up `project4/main.py`.  
2. Built a converter using functions and conditionals.  
3. Tested it for accuracy.  
4. Saved it with Git.

**Why It Matters**: You’re mastering Python’s building blocks, thinking like a programmer, and developing good habits. Ready for Project 5? Let’s keep going!