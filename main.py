"""Console interface for the Student Task Manager."""

from task_manager import TaskManager

MENU = """
===== Student Task Manager =====
1. Add task
2. Display tasks
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


def main():
    manager = TaskManager()
    actions = {"1": handle_add, "2": handle_display}
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


if __name__ == "__main__":
    main()
