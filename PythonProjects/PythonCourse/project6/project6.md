#### Project 6: Student Grades
- **Objective**: Introduce dictionaries.
- **Task**: Create a program that:
  1. Uses a dictionary to store student names (keys) and grades (values).
  2. Allows adding new students and updating grades via a menu.


- **Example Code**:
- <details>
  <summary>Spoiler</summary>

  ```python
  grades = {}
  while True:
      action = input("Add student (A), Update grade (U), Show grades (S), Quit (Q): ").upper()
      if action == 'A':
          name = input("Enter student name: ")
          grade = float(input("Enter grade: "))
          grades[name] = grade
      elif action == 'U':
          name = input("Enter student name: ")
          if name in grades:
              grade = float(input("Enter new grade: "))
              grades[name] = grade
      elif action == 'S':
          for name, grade in grades.items():
              print(f"{name}: {grade}")
      elif action == 'Q':
          break
  ```
  </details>
  

- **Folder**: `project6/`
