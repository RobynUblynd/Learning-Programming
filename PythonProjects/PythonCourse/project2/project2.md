#### Project 2: Simple Calculator
- **Objective**: Learn about variables, data types, and basic operations.
- **Task**: Create a program that:
  1. Asks the user for two numbers and an operation (+, -, *, /).
  2. Performs the operation and displays the result.


- **Example Code**:
- <details>
  <summary>Spoiler</summary>

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
  </details>


- **Folder**: `project2/`
