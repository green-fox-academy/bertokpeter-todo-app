import sys
from todo_app_view import TodoView

class TodoController(TodoView):
    
    def __init__(self):
        self.user_command()
    
    def get_arguments(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return None

    def user_command(self):
        if self.get_arguments() == None:
            self.print_usage()

todo = TodoController()