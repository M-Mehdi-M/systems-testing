# task_manager.py

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = {'description': description, 'done': False}
        self.tasks.append(task)

    def list_tasks(self):
        output = []
        for idx, task in enumerate(self.tasks, start=1):
            status = "DONE" if task['done'] else "TODO"
            output.append(f"{idx}. [{status}] {task['description']}")
        return "\n".join(output)

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True
        else:
            raise IndexError("Invalid task index")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Invalid task index")

    def edit_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['description'] = new_description
        else:
            raise IndexError("Invalid task index")
