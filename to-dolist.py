import json

# Task Class Definition
class Task:
    def _init_(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'completed': self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'], data['category'])
        task.completed = data['completed']
        return task

# File Handling: Save and Load Tasks
def save_tasks(tasks, filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=4)

def load_tasks(filename='tasks.json'):
    try:
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            return [Task.from_dict(data) for data in tasks_data]
    except FileNotFoundError:
        return []

# Display Menu Options
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

# Adding a Task
def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    category = input("Enter task category (Work, Personal, Urgent): ")
    task = Task(title, description, category)
    tasks.append(task)
    print("\nTask added successfully!")

# Viewing All Tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks to display.")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks):
        status = "Completed" if task.completed else "Pending"
        print(f"{idx + 1}. {task.title} - {task.category} [{status}]")
        print(f"   Description: {task.description}")

# Marking a Task as Completed
def mark_task_completed(tasks):
    if not tasks:
        print("\nNo tasks to mark.")
        return
    view_tasks(tasks)
    task_num = int(input("\nEnter the number of the task to mark as completed: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num].mark_completed()
        print("\nTask marked as completed!")
    else:
        print("Invalid task number!")

# Deleting a Task
def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.")
        return
    view_tasks(tasks)
    task_num = int(input("\nEnter the number of the task to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        del tasks[task_num]
        print("\nTask deleted successfully!")
    else:
        print("Invalid task number!")

# Main Function to Run the To-Do List Application
def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("\nTasks saved. Exiting the program.")
            break
        else:
            print("\nInvalid choice, please try again.")

# Run the Program
if _name_ == "_main_":
    main()