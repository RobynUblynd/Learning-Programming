#### Project 3: Number Guessing Game
- **Objective**: Introduce control structures (loops and conditionals).
- **Task**: Implement a game where:
  1. The computer generates a random number between 1 and 100 (use `random.randint(1, 100)`).
  2. The user guesses the number, receiving hints like "Too high" or "Too low" until they guess correctly.


- **Example Code**:
- <details>
  <summary>Spoiler</summary>

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

</details>  

- **Folder**: `project3/`
