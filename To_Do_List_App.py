class To_Do_List:
    def __init__(self):
        self.tasks = []
        
    # Defining the methods    
    def add_task(self, task):
        # Add a new task
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")
        
    def show_tasks(self):
        # Display all tasks in the list
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['task']}")
    
    def mark_task_as_completed(self, index):
        # Mark a task as completed
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
    
    def task_status(self):
        # Display task status
        for i, task in enumerate(self.tasks, 1):
            status = "✔" if task["completed"] else "✘"
            print(f"{i}. {task['task']} - Status: {status}")
    
    def delete_task(self, index):
        # Delete a task from the list
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)


    
# Creating an instance
my_to_do_list = To_Do_List()
