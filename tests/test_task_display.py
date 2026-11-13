import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from rich.console import Console
from src.task_display import TaskDisplay
from src.task import Task


class TestTaskDisplay(unittest.TestCase):

    def setUp(self):

        self.console = Console(record=True, width=100)
        self.task_display = TaskDisplay(self.console)

    def test_display_tasks(self):
        tasks = [
            Task("Test Task", "Test Description", "12-12-2024", "pending")
        ]

        self.task_display.display_tasks(tasks)

        output = self.console.export_text()

        self.assertIn("List of Tasks", output)
        self.assertIn("Test Task", output)
        self.assertIn("Test Description", output)
        self.assertIn("12-12-2024", output)
        self.assertIn("pending", output)

    def test_display_empty_tasks(self):
        self.task_display.display_tasks([])

        output = self.console.export_text()

        self.assertIn("No tasks found.", output)

    def test_display_options(self):
        self.task_display.display_options()

        output = self.console.export_text()

        self.assertIn("Add Task", output)
        self.assertIn("Delete Task", output)
        self.assertIn("List Tasks", output)
        self.assertIn("Exit", output)

    def test_display_task_added(self):
        self.task_display.display_task_added(
            "Test Task",
            "Test Description",
            "12-12-2024"
        )

        output = self.console.export_text()

        self.assertIn("Task Created Successfully", output)
        self.assertIn("Test Task", output)
        self.assertIn("Test Description", output)
        self.assertIn("12-12-2024", output)


if __name__ == "__main__":
    unittest.main()