import sys
from todo_app_view import TodoView
from todo_app_model import TodoModel

class TodoController():
    
    def __init__(self):
        self.view = TodoView()
        self.model = TodoModel()
        self.user_command()
    
    def get_arguments(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return None

    def user_command(self):
        self.arg = self.get_arguments()
        if self.arg == None:
            self.view.print_usage()
        elif self.arg == "-l":
            self.view.print_list(self.model.todo_list)
        elif self.arg == "-a":
            self.add(sys.argv[2])

    def add(self, task):
        with open("todos.txt", "a") as self.file:
            self.file.write(task)
    


todo = TodoController()