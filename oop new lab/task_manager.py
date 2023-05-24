class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, task_name):
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True
                break

    def get_task_details(self, task_name):
        for task in self.tasks:
            if task['name'] == task_name:
                return task
        return None