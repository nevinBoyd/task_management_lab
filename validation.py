from datetime import datetime

# Validate the title is not empty
def validate_task_title(title):
    if title and len(title.strip()) > 0:
        return True
    return False

# Validate description >= 5 characters
def validate_task_description(description):
    if description and len(description.strip()) >= 5:
        return True
    return False

# Validate due date 
def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
