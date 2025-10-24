from datetime import datetime

def validate_task_title(title):
    if not title or len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    return True

def validate_task_description(description):
    if not description or len(description.strip()) < 5:
        raise ValueError("Description must be at least 5 characters long.")
    return True

def validate_due_date(due_date):
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
        return True
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

if len("description") > 500:
    pass
