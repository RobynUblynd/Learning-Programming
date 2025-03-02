Below is a detailed walkthrough for **Project 10: Simple Text-Based Adventure Game**, designed to guide you through creating an interactive text-based adventure game using Python. This project is beginner-friendly and will help you practice key programming concepts like dictionaries, loops, conditionals, and functions, while introducing you to game logic and player choices. By the end, you’ll have a fully functional game where players navigate through rooms, make decisions, and interact with the environment.

---

## Objective
- Learn how to use **dictionaries** to represent game rooms and their connections.
- Practice **loops** and **conditionals** to control game flow and handle player choices.
- Organize code with **functions** for clarity and reusability.
- Validate user input to ensure the game runs smoothly.

## Task
Create a simple text-based adventure game that:
1. Defines multiple rooms, each with a description and possible directions to move (e.g., north, south, east, west).
2. Allows the player to move between rooms by entering directions.
3. Provides feedback on the current room and available exits.
4. Ends the game when the player reaches a specific room or chooses to quit.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Let’s set up your workspace to keep things organized.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: A folder to hold all your course projects.  
  - **How**: If you don’t have it, open PyCharm, go to **File > New Project**, name it `PythonCourse`, choose a location (e.g., Desktop), and click **Create**.  
  - **Why**: Keeps all your projects in one place.

- **Subfolder for Project 10 (`project10/`)**  
  - **What**: A dedicated folder for this project.  
  - **How**: In PyCharm’s Project Explorer (left panel), right-click `PythonCourse`, select **New > Directory**, and name it `project10`.  
  - **Why**: Separates this project from others.

- **Python File (`main.py`)**  
  - **What**: The file where you’ll write your code.  
  - **How**: Right-click `project10/`, choose **New > Python File**, and name it `main.py`.  
  - **Why**: `main.py` is a common name for the main script.

**Your Structure Should Look Like This**:
```
PythonCourse/
├── project1/
│   └── main.py
├── project2/
│   └── main.py
├── ...
└── project10/
    └── main.py
```

---

### Step 2: Write the Code
Now, let’s build the adventure game! Open `main.py` in the `project10/` folder and add the following code:

```python
def describe_room(room):
    print(room["description"])
    print("Exits:", " ".join(room["exits"].keys()))

def move_to_room(current_room, direction, rooms):
    if direction in current_room["exits"]:
        return rooms[current_room["exits"][direction]]
    else:
        print("You can't go that way.")
        return current_room

def play_game():
    rooms = {
        "start": {
            "description": "You are in a dark room. There is a door to the north.",
            "exits": {"north": "hallway"}
        },
        "hallway": {
            "description": "You are in a long hallway. There are doors to the south and east.",
            "exits": {"south": "start", "east": "kitchen"}
        },
        "kitchen": {
            "description": "You are in a kitchen. There is a door to the west and a staircase going up.",
            "exits": {"west": "hallway", "up": "bedroom"}
        },
        "bedroom": {
            "description": "You are in a cozy bedroom. There is a staircase going down.",
            "exits": {"down": "kitchen"}
        }
    }
    current_room = rooms["start"]

    while True:
        describe_room(current_room)
        if current_room == rooms["bedroom"]:
            print("You found the bedroom! You win!")
            break
        direction = input("Which direction do you want to go? (or 'quit' to exit): ").lower()
        if direction == "quit":
            print("Thanks for playing!")
            break
        current_room = move_to_room(current_room, direction, rooms)

if __name__ == "__main__":
    play_game()
```

#### Breaking Down the Code
Here’s what each part does and why it matters:

- **`describe_room(room)` Function**  
  - **What**: Prints the description of the current room and lists available exits.  
  - **How**: Accesses the "description" and "exits" keys in the room dictionary.  
  - **Why**: Provides the player with essential information about their surroundings.

- **`move_to_room(current_room, direction, rooms)` Function**  
  - **What**: Attempts to move to a new room based on the player’s direction input.  
  - **How**: Checks if the direction is a valid exit in the current room. If yes, returns the new room; otherwise, keeps the player in the current room.  
  - **Why**: Handles player movement and validates directions.

- **`play_game()` Function**  
  - **What**: Runs the entire game.  
  - **How**:  
    1. **Setup**:  
       - `rooms`: A dictionary where each key is a room name, and each value is another dictionary containing the room’s description and exits.  
       - `current_room`: Starts at the "start" room.  
    2. **Game Loop**: Runs until the player wins or quits:  
       - Describes the current room.  
       - Checks if the player has reached the winning room ("bedroom").  
       - Asks for a direction or "quit".  
       - Moves to the new room if the direction is valid.  
  - **Why**: Manages the game’s flow and logic.

- **Main Block**  
  - `if __name__ == "__main__":`: Ensures `play_game()` runs when you execute the file directly.

---

### Step 3: Run and Test the Code
Let’s make sure your game works!

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button (top-right).  
  - The game starts in the console, describing the starting room and available exits.

- **Sample Gameplay**:
  ```
  You are in a dark room. There is a door to the north.
  Exits: north
  Which direction do you want to go? (or 'quit' to exit): north
  You are in a long hallway. There are doors to the south and east.
  Exits: south east
  Which direction do you want to go? (or 'quit' to exit): east
  You are in a kitchen. There is a door to the west and a staircase going up.
  Exits: west up
  Which direction do you want to go? (or 'quit' to exit): up
  You are in a cozy bedroom. There is a staircase going down.
  Exits: down
  You found the bedroom! You win!
  ```

- **Test These Scenarios**:  
  - **Win**: Navigate to the "bedroom".  
  - **Invalid Direction**: Try moving in a direction that doesn’t exist (e.g., "west" from the start).  
  - **Quit**: Enter "quit" to exit the game.  
  - **Loop Back**: Move between rooms multiple times (e.g., hallway to kitchen and back).

- **Why Test?**: Ensures the game handles all cases—winning, invalid moves, and quitting—correctly.

---

### Step 4: Commit Your Changes Using Git
Save your progress with Git to track your work.

- **Initialize Git (If Not Done)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Sets up version control for your project.

- **Commit Your Code**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `main.py`, enter a message like "Completed Project 10: Simple Text-Based Adventure Game", and click **Commit**.  
  - **Why**: Records this milestone so you can revisit or share it later.

---

## What You’ve Learned
- **Dictionaries**: Used to represent rooms and their connections.  
- **Loops**: Kept the game running until the player wins or quits.  
- **Conditionals**: Checked player input and game state.  
- **Functions**: Split the code into manageable pieces.  
- **Input Validation**: Ensured player directions are handled correctly.

---

## Extra Challenges
Want to take it further? Try these:  
- **Add Items**: Let players pick up and use items in certain rooms.  
- **Puzzles**: Require players to solve puzzles to unlock new areas.  
- **Multiple Endings**: Create different outcomes based on player choices.  
- **Room Descriptions**: Add more detailed descriptions or random events in rooms.

---

## Next Steps
- Move on to the next project to build on these skills.  
- Keep using Git to save your progress after each project.

You’ve now built an interactive text-based adventure game and strengthened your Python skills—great job!