class TodoModel():

    def __init__(self):
        self.todo_list = []
        with open("todos.txt", "r") as self.todo_file:
            for line in self.todo_file:
                self.todo_list.append({"checked": False, "name": line.rstrip("\n")})   
