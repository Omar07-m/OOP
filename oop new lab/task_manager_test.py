import unittest
from task_manager import TaskManager

class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        task = {'name': 'Task 1', 'completed': False}
        self.task_manager.add_task(task)
        self.assertEqual(len(self.task_manager.tasks), 1)

    def test_mark_task_complete(self):
        task = {'name': 'Task 1', 'completed': False}
        self.task_manager.add_task(task)
        self.task_manager.mark_task_complete('Task 1')
        self.assertTrue(self.task_manager.get_task_details('Task 1')['completed'])

    def test_get_task_details(self):
        task = {'name': 'Task 1', 'completed': False}
        self.task_manager.add_task(task)
        self.assertEqual(self.task_manager.get_task_details('Task 1'), task)
        self.assertIsNone(self.task_manager.get_task_details('Task 2'))

if __name__ == '__main__':
    unittest.main()