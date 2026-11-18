"""Core logic for the Student Task Manager."""

import json
from dataclasses import asdict, dataclass
from pathlib import Path


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

    def __init__(self, storage_path=None):
        self.storage_path = Path(storage_path) if storage_path else None
        self.tasks = []
        self._next_id = 1
        self.load()

    def add_task(self, title):
        """Add a task after validating its title. Raises ValueError if empty."""
        title = (title or "").strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
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

    # ----- persistence -------------------------------------------------

    def load(self):
        """Load tasks from the JSON file, if one is configured and exists."""
        if not self.storage_path or not self.storage_path.exists():
            return
        data = json.loads(self.storage_path.read_text(encoding="utf-8"))
        self.tasks = [Task(**item) for item in data]
        self._next_id = max((t.id for t in self.tasks), default=0) + 1

    def save(self):
        """Write all tasks to the JSON file, if one is configured."""
        if not self.storage_path:
            return
        data = [asdict(task) for task in self.tasks]
        self.storage_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
