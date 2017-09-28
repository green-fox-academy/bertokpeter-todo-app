import sys
from todo_app_view import TodoView

class TodoController():
    
    def __init__(self):
        self.user_command()
    
    def get_arguments(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return None

    def user_command(self):
        if self.get_arguments() == None:
            print("jujj")

todo = TodoController()