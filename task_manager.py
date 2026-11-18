"""Core logic for the Student Task Manager."""

from dataclasses import dataclass


@dataclass
class Task:
    """A single student task."""

    id: int
    title: str
    completed: bool = False

    def __str__(self):
        mark = "x" if self.completed else " "
        return f"[{mark}] {self.id}. {self.title}"


class TaskManager:
    """Keeps the list of tasks and the operations on it."""

    def __init__(self):
        self.tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = Task(id=self._next_id, title=title)
        self.tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return task
        return None
