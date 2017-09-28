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
        elif self.arg == "-r":
            self.remove(sys.argv[2])

    def add(self, task):
        with open("todos.txt", "a") as self.file:
            self.file.write(task + "\n")
    
    def remove(self, index):
        self.model.todo_list.remove(self.model.todo_list[index-1])
        with open("todos.txt", "w") as self.file:
            for element in self.model.todo_list:
                self.file.write(element["name"] + "\n")


todo = TodoController()