Below is a detailed walkthrough for **Project 9: Hangman Game**, designed to guide you through creating an interactive Hangman game using Python. This project is beginner-friendly and will help you practice key programming concepts like lists, loops, conditionals, and functions, while introducing you to random selection and input validation. By the end, you’ll have a fully functional game where players guess letters to reveal a hidden word, with feedback on their progress and a limited number of attempts.

---

## Objective
- Learn how to use **lists** to track the game’s state.
- Practice **loops** and **conditionals** to control gameplay.
- Organize code with **functions** for clarity and reusability.
- Use the **random** module to pick a word unpredictably.
- Validate user input to ensure guesses are single letters.

## Task
Create a Hangman game that:
1. Randomly selects a word from a predefined list.
2. Lets the user guess one letter at a time.
3. Shows the current state of the word (e.g., `_ _ _ _ _` for a 5-letter word).
4. Gives feedback on whether the guessed letter is in the word.
5. Tracks incorrect guesses, limiting the user to 6 attempts.
6. Ends when the user guesses the word or runs out of attempts.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Let’s set up your workspace to keep things organized.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: A folder to hold all your course projects.  
  - **How**: If you don’t have it, open PyCharm, go to **File > New Project**, name it `PythonCourse`, choose a location (e.g., Desktop), and click **Create**.  
  - **Why**: Keeps all your projects in one place.

- **Subfolder for Project 9 (`project9/`)**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click `PythonCourse`, select **New > Directory**, and name it `project9`.  
  - **Why**: Separates this project from others.

- **Python File (`main.py`)**  
  - **What**: The file where you’ll write your code.  
  - **How**: Right-click `project9/`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a common name for the main script.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
└── project9/
    └── main.py
```

---

### Step 2: Write the Code
Now, let’s build the Hangman game! Open `main.py` in the `project9/` folder and add the following code:

```python
import random

def select_word(word_list):
    return random.choice(word_list)

def get_guess():
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Please enter a single letter.")

def play_hangman():
    word_list = ["python", "java", "ruby", "javascript", "html", "css"]
    word = select_word(word_list)
    word_display = ["_" for _ in word]
    guessed_letters = set()
    attempts = 6

    while attempts > 0 and "_" in word_display:
        print(" ".join(word_display))
        print(f"Attempts left: {attempts}")
        guess = get_guess()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    word_display[i] = guess
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Incorrect guess.")

    if "_" not in word_display:
        print(f"Congratulations! You guessed the word: {word}")
    else:
        print(f"Game over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()
```

#### Breaking Down the Code
Here’s what each part does and why it matters:

- **Imports**  
  - `import random`: Brings in the `random` module to pick a word randomly.

- **`select_word(word_list)` Function**  
  - **What**: Picks a random word from `word_list` using `random.choice()`.  
  - **Why**: Makes every game unique and unpredictable.

- **`get_guess()` Function**  
  - **What**: Asks the user for a letter and ensures it’s valid.  
  - **How**: Uses a `while` loop to keep asking until the input is a single alphabetic character (checked with `len(guess) == 1` and `guess.isalpha()`). Converts it to lowercase with `.lower()` for consistency.  
  - **Why**: Prevents errors from invalid inputs like numbers or multiple characters.

- **`play_hangman()` Function**  
  - **What**: Runs the entire game.  
  - **How**:  
    1. **Setup**:  
       - `word_list`: A list of possible words.  
       - `word`: The randomly chosen word to guess.  
       - `word_display`: A list of underscores (`_`) matching the word’s length (e.g., `_ _ _ _ _ _` for "python").  
       - `guessed_letters`: A `set` to track guessed letters.  
       - `attempts`: Starts at 6, decreases with incorrect guesses.  
    2. **Game Loop**: Runs while `attempts > 0` and there are still underscores (`"_"`) in `word_display`:  
       - Shows the current word state (e.g., `p _ _ _ o _`).  
       - Displays remaining attempts.  
       - Gets a guess from the user.  
       - Handles the guess:  
         - If already guessed: Gives a warning.  
         - If correct: Updates `word_display` at all matching positions.  
         - If incorrect: Reduces `attempts` by 1.  
    3. **End Game**:  
       - If no underscores remain: User wins.  
       - If attempts hit zero: User loses.  
  - **Why**: Ties everything together in a clear, manageable way.

- **Main Block**  
  - `if __name__ == "__main__":`: Ensures `play_hangman()` runs when you execute the file directly.

---

### Step 3: Run and Test the Code
Let’s make sure your game works!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button (top-right).  
  - The game starts in the console, showing the word as underscores and your attempts.

- **Sample Gameplay**:
  ```
  _ _ _ _ _ _
  Attempts left: 6
  Guess a letter: p
  p _ _ _ _ _

  Attempts left: 6
  Guess a letter: q
  Incorrect guess.
  p _ _ _ _ _

  Attempts left: 5
  Guess a letter: y
  p y _ _ _ _

  Attempts left: 5
  Guess a letter: t
  p y t _ _ _

  Attempts left: 5
  Guess a letter: h
  p y t h _ _

  Attempts left: 5
  Guess a letter: o
  p y t h o _

  Attempts left: 5
  Guess a letter: n
  Congratulations! You guessed the word: python
  ```

- **Test These Scenarios**:  
  - **Win**: Guess the word fully (e.g., "python").  
  - **Lose**: Make 6 incorrect guesses.  
  - **Repeat Guess**: Guess the same letter twice (e.g., "p" then "p" again).  
  - **Invalid Input**: Try numbers (e.g., "5") or multiple letters (e.g., "ab").  
  - **Repeated Letters**: Pick a word like "java" and guess "a" to see both revealed.

- **Why Test?**: Ensures the game handles all cases—winning, losing, and errors—correctly.

---

### Step 4: Commit Your Changes Using Git
Save your progress with Git to track your work.

- **Initialize Git (If Not Done)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Sets up version control for your project.

- **Commit Your Code**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, enter a message like "Completed Project 9: Hangman Game", and click **Commit**.  
  - **Why**: Records this milestone so you can revisit or share it later.

---

## What You’ve Learned
- **Lists**: Used `word_display` to show the word’s state.  
- **Sets**: Tracked guesses with `guessed_letters`.  
- **Loops**: Kept the game running until it ends.  
- **Conditionals**: Checked guesses and game outcomes.  
- **Functions**: Split the code into manageable pieces.  
- **Random**: Added variety with `random.choice()`.  
- **Input Validation**: Ensured guesses are valid.

---

## Extra Challenges
Want to take it further? Try these:  
- **More Words**: Add to `word_list` (e.g., "kotlin", "swift").  
- **Hangman Figure**: Print a drawing that updates with wrong guesses.  
- **Difficulty Levels**: Offer easy (short words), medium, or hard (longer words).  
- **Score Tracking**: Award points based on remaining attempts.

---

## Next Steps
- Move on to **Project 10** to build on these skills.  
- Keep using Git to save your progress after each project.

You’ve now built a fun, interactive Hangman game and strengthened your Python skills—great job!