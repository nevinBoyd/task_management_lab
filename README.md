# Task Management System

## 📘 Overview

This project is a **Python-based Task Management System** built as part of the Flatiron School Module 6 Lab: _Functions, Libraries, and Input Validation._

The program allows users to:

- Add tasks with a title, description, and due date
- Mark tasks as complete
- View pending tasks
- Track progress as a completion percentage

It reinforces key Python concepts including:

- Functions and modular programming
- Importing and reusing modules
- Data validation using `datetime`
- Lists and dictionaries for data storage

---

## Features

- **Add Task:** Create new tasks with validation for title, description, and due date.
- **Mark Complete:** Update a task’s status once it’s done.
- **View Pending:** Display all tasks that are not yet completed.
- **Progress Tracker:** Calculate and show overall completion percentage.

---

## Technologies Used

- **Python 3.12**
- Built-in modules only (`datetime`)
- No external libraries required

---

## How to Run

1. Clone this repository or download the ZIP.
2. Open a terminal in the project folder.
3. Run:

   ```
   python3 main.py

   ```

### Example

```
Task Management System
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View Progress
5. Exit
Enter your choice (1-5): 1
Enter task title: music listen
Enter task desription: review music for upcoming film
Enter due date (YYYY-MM-DD): 2026-01-16
Task add successfully!
Task Management System
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View Progress
5. Exit
Enter your choice (1-5): 4
Task completion progress: 0.0%
Task Management System
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View Progress
5. Exit
Enter your choice (1-5): 3

Pending Tasks.
1. music listen (Due: 2026-01-16)
Task Management System
1. Add Task
2. Mark Task as Complete
3. View Pending Tasks
4. View Progress
5. Exit
Enter your choice (1-5): 5
Exiting the program...

```

---

### Validation Rules

Title: Cannot be empty.

Description: Must be at least 5 characters long.

Due Date: Must match YYYY-MM-DD format.

---

## Templates and Structure

This project was built using the provided Flatiron School **Task Management System** templates.  
The following starter files were included and then expanded with custom logic and validation:

- `main.py` – base menu and control flow
- `task_utils.py` – placeholder functions for task logic
- `validation.py` – input validation scaffolding

---

## Resources and References

- [Python Official Documentation – datetime](https://docs.python.org/3/library/datetime.html)
- [Real Python – Modules and Packages](https://realpython.com/python-modules-packages/)
- [Flatiron School – Module 6: Functions and Input Validation](https://flatironschool.com/courses/792/modules) _requires credentials for access_
- [MDN – Program Flow Basics](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/conditionals)
