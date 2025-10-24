# Import functions from task_manager.task_utils package
from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress
# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
           # Gather task input
           title = input("Enter your choice (1-5): ")
           description = input("Enter task desription: ")
           due_date = input("Enter due date (YYYY-MM-DD): ")
   
           # Add new task
           add_task(title, description, due_date)

        elif choice == "2":
           # View tasks to mark complete
           view_pending_tasks()
           index = int(input("Enter the number to mark as complete: "))
   
           # Mark as complete
           mark_task_as_complete(index)

        elif choice == "3":
           # View pending tasks
           view_pending_tasks()

        elif choice == "4":
            # View progress
            progress= calculate_progress()
            print(f"Task completion progress: {progress}%")    

        elif choice == "5":            
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run main if executed directly
if __name__ == "__main__":
    main()
