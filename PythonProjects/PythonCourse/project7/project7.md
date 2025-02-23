#### Project 7: File Handling
- **Objective**: Learn file operations.
- **Task**: Write a program that:
  1. Reads content from an input file (e.g., `input.txt`).
  2. Writes the content to an output file (e.g., `output.txt`), optionally modifying it (e.g., converting to uppercase).


- **Example Code**:
- <details>
  <summary>Spoiler</summary>

   ```python
  with open('input.txt', 'r') as infile:
      content = infile.read()
  with open('output.txt', 'w') as outfile:
      outfile.write(content.upper())
  print("File has been copied and converted to uppercase.")
  ```
  </details>  


- **Folder**: `project7/` (Create an `input.txt` file in this folder to test)
