class TodoView():

    def print_usage(self):
        print("\n\
               Command Line Todo application\n\
               =============================\n\
               \n\
               Command line arguments:\n\
               -l   Lists all the tasks\n\
               -a   Adds a new task\n\
               -r   Removes an task\n\
               -c   Completes an task")

    def print_list(self, dict_list):
        for i in range(len(dict_list)):
            task = dict_list[i]["name"]
            check = "x" if dict_list[i]["checked"] else " "
            print(str(i+1) + " - [" + check + "] " + task)
