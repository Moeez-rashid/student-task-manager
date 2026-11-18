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
    try:
        task = manager.add_task(title)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Added task {task.id}: {task.title}")


def handle_display(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        print(task)


def handle_complete(manager):
    raw = input("Task id(s) to complete, separated by commas: ")
    try:
        task_ids = [int(part) for part in raw.split(",") if part.strip()]
    except ValueError:
        print("Error: please enter numeric task ids, e.g. 1,3")
        return
    completed, already_done, not_found = manager.complete_tasks(task_ids)
    for task_id in completed:
        print(f"Task {task_id} marked as completed.")
    for task_id in already_done:
        print(f"Task {task_id} was already completed.")
    for task_id in not_found:
        print(f"Task {task_id} not found.")


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
