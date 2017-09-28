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
            try:
                self.add(sys.argv[2])
            except IndexError:
                print("Unable to add: no task provided")
        elif self.arg == "-r":
            try:
                self.remove(sys.argv[2])
            except IndexError:
                if len(sys.argv) > 2:
                    print("Unable to remove: index out of bound")
                else:
                    print("Unable to remove: no index provided")
            except ValueError:
                print("Unable to remove: index is not a number")
        elif self.arg == "-c":
            try:
                self.check(sys.argv[2])
            except IndexError:
                if len(sys.argv) > 2:
                    print("Unable to check: index out of bound")
                else:
                    print("Unable to check: no index provided")
            except ValueError:
                print("Unable to remove: index is not a number")
        else:
            self.view.arg_error()

    def add(self, task):
        with open("todos.txt", "a") as self.file:
            self.file.write("0 " + task + "\n")
    
    def remove(self, index):
        self.model.todo_list.remove(self.model.todo_list[int(index)-1])
        self.model.write()

    def check(self, index):
        self.model.todo_list[int(index)-1]["checked"] = True
        self.model.write()

todo = TodoController()