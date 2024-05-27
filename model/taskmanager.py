class ToDoTask:
    def __init__(self, description, date=None, time=None):
        self.description = description  
        self.date = date  
        self.time = time
        self.completed = False