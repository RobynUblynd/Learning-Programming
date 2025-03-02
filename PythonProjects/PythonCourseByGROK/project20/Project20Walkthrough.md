Below is a detailed walkthrough for **Project 20: Contact Book Application**, formatted in a style consistent with a typical project walkthrough (e.g., `Project10Walkthrough.md`). This guide will walk you through creating a simple contact book application in Python, integrating concepts like object-oriented programming (OOP), file handling, and user interaction. By the end, you’ll have a functional program that allows users to add, view, search, and delete contacts, with data saved to a JSON file for persistence.

---

## Objective
- Combine multiple Python concepts (OOP, file handling, and user input) into a cohesive, practical application.
- Build a menu-driven program with intuitive user interactions.
- Learn to persist and retrieve data using JSON to maintain contact information across sessions.

## Task
Develop a contact book application that:
1. Uses a `Contact` class to represent individual contacts with attributes like name and phone number.
2. Manages a collection of contacts within a `ContactBook` class.
3. Provides a menu interface for users to add, view, search, and delete contacts.
4. Saves contact data to a JSON file and loads it when the program starts.

---

## Step-by-Step Guide

### Step 1: Create the Project Structure
Organize your workspace to keep your code modular and tidy.

- **Main Project Directory (`PythonCourse`)**  
  - **What**: The root folder for all your course projects.  
  - **How**: If it doesn’t exist, open PyCharm, go to **File > New Project**, name it `PythonCourse`, choose a location (e.g., Desktop), and click **Create**. If it already exists, open it via **File > Open** and select `PythonCourse`.  
  - **Why**: Keeps all your projects centralized for easy access and management.

- **Subfolder for Project 20 (`project20/`)**  
  - **What**: A dedicated folder for this project’s files.  
  - **How**: In PyCharm’s Project Explorer, right-click `PythonCourse`, select **New > Directory**, and name it `project20`.  
  - **Why**: Isolates Project 20’s files from other projects, improving organization.

- **Python Files (`contact.py` and `main.py`)**  
  - **What**: `contact.py` will contain the `Contact` and `ContactBook` class definitions, while `main.py` will handle the main application logic.  
  - **How**: Right-click `project20/`, choose **New > Python File**, and create `contact.py`. Repeat the process to create `main.py`.  
  - **Why**: Separating class definitions from the application logic enhances modularity and readability.

**Expected Directory Structure**:
```
PythonCourse/
├── project1/
│   └── main.py
├── ...
├── project19/
│   └── main.py
└── project20/
    ├── contact.py
    └── main.py
```

---

### Step 2: Define the `Contact` Class
Create a simple class to represent individual contacts.

- **What**: A `Contact` class with attributes for a contact’s name and phone number.  
- **How**: Open `contact.py` in the `project20/` folder and add the following code:  
  ```python
  class Contact:
      def __init__(self, name, phone):
          self.name = name
          self.phone = phone
  ```  
- **Why**:  
  - **Encapsulation**: Groups contact-related data (name and phone) into a single object.  
  - **Extensibility**: Makes it easy to add more attributes (e.g., email or address) later if needed.

---

### Step 3: Define the `ContactBook` Class
Create a class to manage a list of contacts, including methods for core operations and file handling.

- **What**: A `ContactBook` class with methods to add, view, search, and delete contacts, plus save and load them from a JSON file.  
- **How**: Add the following code to `contact.py` below the `Contact` class:  
  ```python
  import json

  class ContactBook:
      def __init__(self):
          self.contacts = []
          self.load_contacts()

      def add_contact(self, name, phone):
          contact = Contact(name, phone)
          self.contacts.append(contact)
          print(f"Added contact: {name}")

      def view_contacts(self):
          if not self.contacts:
              print("No contacts found.")
          else:
              for i, contact in enumerate(self.contacts, 1):
                  print(f"{i}. {contact.name}: {contact.phone}")

      def search_contacts(self, query):
          results = [c for c in self.contacts if query.lower() in c.name.lower()]
          if not results:
              print("No matching contacts found.")
          else:
              for contact in results:
                  print(f"{contact.name}: {contact.phone}")

      def delete_contact(self, name):
          for contact in self.contacts:
              if contact.name.lower() == name.lower():
                  self.contacts.remove(contact)
                  print(f"Deleted contact: {name}")
                  return
          print(f"Contact not found: {name}")

      def save_contacts(self):
          with open("contacts.json", "w") as f:
              json.dump([{"name": c.name, "phone": c.phone} for c in self.contacts], f)
          print("Contacts saved.")

      def load_contacts(self):
          try:
              with open("contacts.json", "r") as f:
                  data = json.load(f)
                  self.contacts = [Contact(d["name"], d["phone"]) for d in data]
          except FileNotFoundError:
              self.contacts = []
  ```  
- **Why**:  
  - **Core Functionality**: Methods like `add_contact`, `view_contacts`, `search_contacts`, and `delete_contact` provide the main features of the contact book.  
  - **Persistence**: `save_contacts` serializes the contact list to a JSON file, and `load_contacts` restores it, ensuring data isn’t lost when the program closes.  
  - **Efficiency**: Uses list comprehensions for filtering (`search_contacts`) and JSON serialization (`save_contacts`), making the code concise and readable.

---

### Step 4: Implement the Main Application Logic
Build a menu-driven interface in `main.py` to let users interact with the `ContactBook` class.

- **What**: A loop that displays a menu and processes user input to call the appropriate `ContactBook` methods.  
- **How**: Open `main.py` in the `project20/` folder and add this code:  
  ```python
  from contact import ContactBook

  def main():
      book = ContactBook()

      while True:
          print("\n--- Contact Book Menu ---")
          print("1. Add Contact")
          print("2. View Contacts")
          print("3. Search Contacts")
          print("4. Delete Contact")
          print("5. Save and Exit")

          choice = input("Enter your choice (1-5): ")

          if choice == "1":
              name = input("Enter name: ")
              phone = input("Enter phone: ")
              book.add_contact(name, phone)
          elif choice == "2":
              book.view_contacts()
          elif choice == "3":
              query = input("Enter search query: ")
              book.search_contacts(query)
          elif choice == "4":
              name = input("Enter name to delete: ")
              book.delete_contact(name)
          elif choice == "5":
              book.save_contacts()
              print("Exiting...")
              break
          else:
              print("Invalid choice. Please try again.")

  if __name__ == "__main__":
      main()
  ```  
- **Why**:  
  - **User-Friendly**: The menu provides clear options, making the program accessible to users.  
  - **Control Flow**: The `while` loop keeps the program running until the user chooses to exit.  
  - **Separation of Concerns**: Keeps the application logic separate from the class definitions, improving maintainability.

---

### Step 5: Run and Test the Application
Verify that your program works as intended by testing all features.

- **How to Run**:  
  - In PyCharm, right-click `main.py` and select **Run 'main'**, or click the green "Play" button in the toolbar.  
  - The menu will appear in the console, prompting you to select an option.

- **Test Cases**:  
  1. **Add Contact**: Select option 1, enter a name (e.g., "Alice") and phone number (e.g., "123-456-7890"). Check the confirmation message.  
  2. **View Contacts**: Select option 2 to see the list of contacts you’ve added.  
  3. **Search Contacts**: Select option 3, enter a partial name (e.g., "Ali") to find matching contacts.  
  4. **Delete Contact**: Select option 4, enter a name (e.g., "Alice") to remove it, and confirm deletion.  
  5. **Save and Exit**: Select option 5 to save contacts and exit.

- **Persistence Test**:  
  - Add a few contacts, save, and exit. Restart the program and select option 2; the contacts should still be listed, loaded from `contacts.json`.

- **Why Test**: Confirms that all features function correctly and that data persistence works across program runs.

---

### Step 6: Commit Your Work with Git
Use version control to save your progress (optional but recommended).

- **Enable Git (If Needed)**:  
  - **How**: In PyCharm, go to **VCS > Enable Version Control Integration**, select **Git**, and click **OK**.  
  - **Why**: Initializes Git for your project if it hasn’t been set up yet.

- **Commit Changes**:  
  - **How**: Press `Ctrl + K` (Windows/Linux) or `Cmd + K` (Mac), check `contact.py` and `main.py`, enter a commit message like "Completed Project 20: Contact Book Application", and click **Commit**.  
  - **Why**: Saves your work in a version-controlled history, allowing you to track changes or revert if needed.

---

## Complete Code for `contact.py`
Here’s the full code for `contact.py`:

```python
import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load_contacts()

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"Added contact: {name}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name}: {contact.phone}")

    def search_contacts(self, query):
        results = [c for c in self.contacts if query.lower() in c.name.lower()]
        if not results:
            print("No matching contacts found.")
        else:
            for contact in results:
                print(f"{contact.name}: {contact.phone}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Deleted contact: {name}")
                return
        print(f"Contact not found: {name}")

    def save_contacts(self):
        with open("contacts.json", "w") as f:
            json.dump([{"name": c.name, "phone": c.phone} for c in self.contacts], f)
        print("Contacts saved.")

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as f:
                data = json.load(f)
                self.contacts = [Contact(d["name"], d["phone"]) for d in data]
        except FileNotFoundError:
            self.contacts = []
```

---

## Complete Code for `main.py`
Here’s the full code for `main.py`:

```python
from contact import ContactBook

def main():
    book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Delete Contact")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            book.add_contact(name, phone)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            query = input("Enter search query: ")
            book.search_contacts(query)
        elif choice == "4":
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == "5":
            book.save_contacts()
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

---

## What You’ve Learned
- **Object-Oriented Programming**: Used classes (`Contact` and `ContactBook`) to structure and manage contact data.  
- **File Handling**: Implemented JSON-based persistence to save and load contacts between sessions.  
- **User Interaction**: Built a menu-driven interface for seamless user experience.  
- **Data Management**: Enabled adding, viewing, searching, and deleting contacts with straightforward commands.

---

## Extra Challenges
Take your application further with these optional enhancements:  
- **Edit Contacts**: Add a menu option to modify existing contact details.  
- **Input Validation**: Ensure phone numbers contain only digits or follow a specific format.  
- **Sorting**: Allow users to sort contacts alphabetically by name or numerically by phone number.

---

## Next Steps
- Reflect on how OOP, file handling, and user interaction integrate in this project.  
- Explore building a more advanced version, such as a graphical contact book using Python’s `tkinter` library.

Congratulations! You’ve successfully completed Project 20 and built a practical contact book application, showcasing your Python skills in a real-world scenario!