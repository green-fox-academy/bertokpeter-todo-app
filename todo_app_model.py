class TodoModel():

    def __init__(self):
        self.todo_file = open(todos.txt, "r")
        self.todo_list = []
        for line in self.todo_file:
            self.todo_list.append(line)
        self.todo_file.close()        