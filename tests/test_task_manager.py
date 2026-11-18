"""Unit tests for the Student Task Manager core logic."""

import tempfile
import unittest
from pathlib import Path

from task_manager import TaskManager, TaskNotFoundError


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Finish DevOps lab")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish DevOps lab")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_strips_whitespace(self):
        task = self.manager.add_task("   Read chapter 4   ")
        self.assertEqual(task.title, "Read chapter 4")

    def test_add_task_rejects_empty_title(self):
        for title in ["", "    ", None]:
            with self.assertRaises(ValueError):
                self.manager.add_task(title)
        self.assertEqual(self.manager.list_tasks(), [])

    def test_add_task_rejects_too_long_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("x" * 101)


class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        for title in ["Quiz prep", "Assignment", "Project"]:
            self.manager.add_task(title)

    def test_mark_task_complete(self):
        task = self.manager.complete_task(2)
        self.assertTrue(task.completed)
        self.assertTrue(self.manager.get_task(2).completed)
        self.assertFalse(self.manager.get_task(1).completed)

    def test_complete_selected_tasks(self):
        self.manager.complete_task(3)
        completed, already_done, not_found = self.manager.complete_tasks([1, 3, 9])
        self.assertEqual(completed, [1])
        self.assertEqual(already_done, [3])
        self.assertEqual(not_found, [9])


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.manager.add_task("Keep me")
        self.manager.add_task("Delete me")

    def test_delete_task(self):
        deleted = self.manager.delete_task(2)
        self.assertEqual(deleted.title, "Delete me")
        remaining = [task.title for task in self.manager.list_tasks()]
        self.assertEqual(remaining, ["Keep me", "Delete me"])

    def test_delete_unknown_task_raises(self):
        with self.assertRaises(TaskNotFoundError):
            self.manager.delete_task(42)
        self.assertEqual(len(self.manager.list_tasks()), 2)


class TestPersistence(unittest.TestCase):
    def test_tasks_are_saved_and_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            manager = TaskManager(path)
            manager.add_task("Saved task")
            manager.complete_task(1)
            manager.save()

            reloaded = TaskManager(path)
            self.assertEqual(len(reloaded.list_tasks()), 1)
            self.assertTrue(reloaded.get_task(1).completed)
            self.assertEqual(reloaded.add_task("Next").id, 2)


if __name__ == "__main__":
    unittest.main()
