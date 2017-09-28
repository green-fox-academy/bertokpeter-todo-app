class TodoModel():

    def __init__(self):
        self.todo_list = []
        with open("todos.txt", "r") as self.file:
            for line in self.file:
                self.todo_list.append({"checked": line[0] == "1", "name": line[2:].rstrip("\n")})
    
    def write(self):
        with open("todos.txt", "w") as self.file:
            for element in self.todo_list:
                one = "1" if element["checked"] else "0"
                self.file.write(one + " " + element["name"] + "\n")
