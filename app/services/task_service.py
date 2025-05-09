class TaskService:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def create_task(self, task_data):
        return self.task_repository.create_task(task_data)

    def get_task(self, task_id):
        return self.task_repository.get_task(task_id)

    def update_task(self, task_id, task_data):
        return self.task_repository.update_task(task_id, task_data)

    def delete_task(self, task_id):
        return self.task_repository.delete_task(task_id)