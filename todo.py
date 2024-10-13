import json

# Class representing a task in the task manager with title, description, category, and completion status
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False  # Task is initially not completed

    # Method to mark the task as completed
    def mark_completed(self):
        self.completed = True

    # String representation of the task
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} - {self.description} (Category: {self.category})"

# Function to save tasks to a JSON file
def save_tasks(tasks):
    # open the file in write mode
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)

# Function to load tasks from a JSON file
def load_tasks():
    try:
        # open the file in read mode
        with open('tasks.json', 'r') as f:
            # Load JSON data from the file and create Task objects
            tasks = [Task(**task) for task in json.load(f)]
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file not found or JSON is invalid

# Main function to run the task manager
def main():
    tasks = load_tasks()  # Load existing tasks from file
    
    while True:
        # Display menu options
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            # Add a new task
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            category = input("Enter task category: ")
            # Create a new Task object and add it to the list
            tasks.append(Task(title, description, category))
            print("Task added successfully.")
        elif choice == '2':
            # View all tasks
            if tasks:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks available.")
        elif choice == '3':
            # Mark a task as completed
            if tasks:
                # Get the task number from the user and mark it as completed
                task_number = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= task_number < len(tasks):
                    tasks[task_number].mark_completed()
                else:
                    # Display an error message if the task number is invalid
                    print("Invalid task number.")
            else:
                print("No tasks available.")
        elif choice == '4':
            # Delete a task
            if tasks:
                # Get the task number from the user and delete the task
                task_number = int(input("Enter task number to delete: ")) - 1
                if 0 <= task_number < len(tasks):
                    tasks.pop(task_number)
                else:
                    print("Invalid task number.")
            else:
                print("No tasks available.")
        elif choice == '5':
            # Save tasks and exit
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

# Entry point of the script
if __name__ == "__main__":
    main()