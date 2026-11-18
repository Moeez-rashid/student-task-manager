"""Console interface for the Student Task Manager."""

from task_manager import TaskManager, TaskNotFoundError

DATA_FILE = "tasks.json"

MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Mark task as completed
4. Delete task
0. Exit
"""


def handle_add(manager):
    title = input("Task title: ")
    task = manager.add_task(title)
    print(f"Added task {task.id}.")


def handle_display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)


def handle_complete(manager):
    task_id = int(input("Task id to complete: "))
    task = manager.complete_task(task_id)
    if task:
        print(f"Task {task.id} marked as completed.")
    else:
        print("Task not found.")


def handle_delete(manager):
    raw = input("Task id to delete: ").strip()
    if not raw.isdigit():
        print("Error: the task id must be a positive whole number.")
        return
    confirm = input(f"Delete task {raw}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return
    try:
        task = manager.delete_task(int(raw))
    except TaskNotFoundError as error:
        print(f"Error: {error}")
        return
    print(f"Deleted task {task.id}: {task.title}")


def main():
    manager = TaskManager(DATA_FILE)
    actions = {
        "1": handle_add,
        "2": handle_display,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option, try again.")
            continue
        action(manager)
        manager.save()


if __name__ == "__main__":
    main()
