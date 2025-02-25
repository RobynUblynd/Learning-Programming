Below is a detailed walkthrough for **Project 17**, formatted consistently with the style of `Project10Walkthrough.md`. This guide will walk you through creating a Python program to explore **polymorphism** in object-oriented programming by designing a shape-based application. By the end, you’ll have a working program that demonstrates how different shapes can be managed uniformly through a shared interface, highlighting the power of polymorphism.

---

## Objective
- Understand **polymorphism** in object-oriented programming.
- Learn to define a base class with methods that derived classes can override.
- Practice creating and manipulating a list of objects from different classes that inherit from a common base class.

## Task
Create a program that:
1. Defines a base class `Shape` with an `area()` method that returns 0.
2. Implements derived classes `Circle`, `Rectangle`, and `Triangle`, each overriding the `area()` method to compute their specific areas.
3. Demonstrates polymorphism by storing instances of these classes in a list and invoking the `area()` method on each, regardless of the shape type.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Set up an organized workspace for your code.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder containing all your course projects.  
  - **How**: If it doesn’t exist, open PyCharm, go to **File > New Project**, name it `PythonCourse`, select a location (e.g., Desktop), and click **Create**. If it already exists, open it via **File > Open** and select `PythonCourse`.  
  - **Why**: Keeps all your projects centralized for easy management.

- **Subfolder for Project 17 (`project17/`)**  
  - **What**: A dedicated folder for this project’s files.  
  - **How**: In PyCharm’s Project Explorer, right-click `PythonCourse`, select **New > Directory**, and name it `project17`.  
  - **Why**: Isolates Project 17’s files to maintain clarity.

- **Python File (`main.py`)**  
  - **What**: The script where you’ll write your code.  
  - **How**: Right-click `project17/`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a conventional name for the primary script.

**Expected Structure**:
```
PythonCourse/
├── project1/
│   └── main.py
├── ...
├── project16/
│   ├── accounts.py
│   └── main.py
└── project17/
    └── main.py
```

---

### Step 2: Define the Base Class `Shape`
Create a base class that establishes a common interface for all shapes.

- **What**: A `Shape` class with an `area()` method returning 0 as a default.  
- **How**: Open `main.py` in the `project17/` folder and add the following code:  
```python
class Shape:
    def area(self):
        return 0
```
- **Why**:  
  - **Base Class**: Acts as a blueprint for all shapes.  
  - **Polymorphism**: Provides a method (`area()`) that derived classes can override, ensuring a uniform interface.

---

### Step 3: Create Derived Classes
Define specific shape classes that inherit from `Shape` and override the `area()` method with their own calculations.

- **Circle Class**  
  - **What**: A class for a circle, defined by its radius, calculating its area.  
  - **How**: Add this code below the `Shape` class:  
```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2
```
  - **Why**:  
    - **Inheritance**: Extends `Shape` to inherit its structure.  
    - **Override**: Implements the area formula πr² for a circle (using 3.1416 as an approximation of π).

- **Rectangle Class**  
  - **What**: A class for a rectangle, defined by width and height, calculating its area.  
  - **How**: Add this code below `Circle`:  
```python
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
```
  - **Why**:  
    - **Inheritance**: Builds on `Shape`.  
    - **Override**: Calculates area as width × height.

- **Triangle Class**  
  - **What**: A class for a triangle, defined by base and height, calculating its area.  
  - **How**: Add this code below `Rectangle`:  
```python
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
```
  - **Why**:  
    - **Inheritance**: Inherits from `Shape`.  
    - **Override**: Computes area using the formula (base × height)/2.

---

### Step 4: Demonstrate Polymorphism
Showcase polymorphism by managing different shape objects uniformly.

- **What**: Create a list of shape instances and iterate over it to display each shape’s area.  
- **How**: Append this code to the end of `main.py`:  
```python
# Create a list of shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

# Calculate and print the area of each shape
for shape in shapes:
    print(f"The area of the shape is: {shape.area():.2f}")
```
- **Why**:  
  - **Polymorphism**: Allows the `area()` method to be called on each object, executing the appropriate overridden version based on the object’s actual type.  
  - **Scalability**: New shapes can be added to the list without altering the iteration logic.

---

### Step 5: Run and Test the Code
Ensure your program works as intended by running it and checking the output.

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or press the green "Play" button.  
  - The output will display in the console.

- **Expected Output**:
```
The area of the shape is: 78.54
The area of the shape is: 24.00
The area of the shape is: 10.50
```

- **Explanation**:  
  - **Circle**: Area = π × 5² ≈ 78.54 (using 3.1416 for π).  
  - **Rectangle**: Area = 4 × 6 = 24.00.  
  - **Triangle**: Area = 0.5 × 3 × 7 = 10.50.  
  - Each shape correctly uses its overridden `area()` method, demonstrating polymorphism.

- **Why Test**: Verifies that the program accurately computes areas and that polymorphism functions as expected.

---

### Step 6: Commit Your Work with Git
Use version control to save your progress.

- **Enable Git (If Needed)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Initializes Git for your project if it’s not already set up.

- **Commit Changes**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, enter a commit message like "Completed Project 17: Polymorphism with Shapes", and click **Commit**.  
  - **Why**: Records your work in a version-controlled snapshot.

---

## Complete Code for `main.py`
Here’s the full code for your reference:

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Create a list of shapes
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 7)
]

# Calculate and print the area of each shape
for shape in shapes:
    print(f"The area of the shape is: {shape.area():.2f}")
```

---

## What You’ve Learned
- **Polymorphism**: Handled diverse shape objects uniformly via a shared base class.  
- **Method Overriding**: Customized the `area()` method for each shape while preserving a consistent interface.  
- **Object-Oriented Design**: Built a flexible system that can easily accommodate new shapes without modifying existing code.

---

## Extra Challenges
Take your skills further with these optional exercises:  
- **Add More Shapes**: Create classes like `Square` or `Pentagon` and add them to the `shapes` list.  
- **User Input**: Modify the program to accept shape dimensions from the user dynamically.  
- **Shape Properties**: Extend each class with methods to calculate perimeter or other attributes.

---

## Next Steps
- Move on to **Project 18: Generators** to explore efficient iteration techniques in Python.  
- Keep using Git to track your progress in subsequent projects.

Congratulations! You’ve completed Project 17 and gained a solid understanding of polymorphism in Python through this shape-based program!