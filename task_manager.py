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
