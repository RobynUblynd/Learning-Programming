#### Project 4: Temperature Converter
- **Objective**: Learn about functions.
- **Task**: Write a program with two functions:
  1. `c_to_f(celsius)`: Converts Celsius to Fahrenheit.
  2. `f_to_c(fahrenheit)`: Converts Fahrenheit to Celsius.
  3. Ask the user for a temperature and conversion direction, then display the result.


- **Example Code**:
- <details>
  <summary>Spoiler</summary>

  
  ```python
  def c_to_f(celsius):
      return (celsius * 9/5) + 32
  def f_to_c(fahrenheit):
      return (fahrenheit - 32) * 5/9
  choice = input("Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ")
  if choice.upper() == 'C':
      temp = float(input("Enter temperature in Celsius: "))
      print(f"{temp}°C is {c_to_f(temp)}°F")
  else:
      temp = float(input("Enter temperature in Fahrenheit: "))
      print(f"{temp}°F is {f_to_c(temp)}°C")
  ```
</details>


- **Folder**: `project4/`
