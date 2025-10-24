from datetime import datetime
# Import validation functions
from validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    # Validate fields
    if not validate_task_title(title):                                 
       print("Invalid title. Please try again.")
       return
    if not validate_task_description(description):
       print("Invalid description. Please try again")
       return
    if not validate_due_date(due_date):
       print("Invalid due date format. Please use YYYY-MM-DD")
       return

    # Create new task dictionary
    task = {
       "title": title,
       "description": description,
       "due_date": due_date,
       "completed": False
    }

    # Add to global task list
    tasks.append(task)
    print("Task add successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    # Ensure index is valid
    if index < 1 or index > len(tasks):
       print("Invalid task numer.")
       return
    
    # Mark task is done
    tasks[index - 1]["completed"] = True
    print(f"Task '{tasks[index - 1]['title']}' marked as completed!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]

    if not pending:
       print("No pending tasks.")
       return
    
    print("\nPending Tasks.")
    for i, task in enumerate(pending, 1):
        print(f"{i}. {task['title']} (Due: {task['due_date']})")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    
    completed =sum(1 for task in tasks if task["completed"])
    progress = round((completed / len(tasks)) * 100, 2)
    return progress
