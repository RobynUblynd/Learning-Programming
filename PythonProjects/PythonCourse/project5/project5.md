#### Project 5: Simple To-Do List
- **Objective**: Practice using lists and functions.
- **Task**: Create a program that:
  1. Uses a list to store tasks.
  2. Includes functions `add_task(tasks, task)` to add a task and `show_tasks(tasks)` to display all tasks.
  3. Provides a simple menu for user interaction.
 

- **Example Code**:
- <details>
  <summary>Spoiler</summary>

  ```python
  tasks = []
  def add_task(tasks, task):
      tasks.append(task)
  def show_tasks(tasks):
      for i, task in enumerate(tasks, 1):
          print(f"{i}. {task}")
  while True:
      action = input("Add task (A), Show tasks (S), or Quit (Q): ").upper()
      if action == 'A':
          task = input("Enter task: ")
          add_task(tasks, task)
      elif action == 'S':
          show_tasks(tasks)
      elif action == 'Q':
          break
  ```
  </details>


- **Folder**: `project5/`
