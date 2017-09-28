class TodoView():

    def print_usage(self):
        print("\n\
               Command Line Todo application\n\
               =============================\n\
               \n\
               Command line arguments:\n\
               -l    Lists undone tasks\n\
               -la   Lists all the tasks\n\
               -a    Adds a new task\n\
               -r    Removes an task\n\
               -c    Completes an task")

    def print_list(self, dict_list, list_all):
        original_list = dict_list
        if not list_all:
            dict_list = [elem for elem in dict_list if not elem["checked"]]
        if len(dict_list) == 0:
            print("No todos for today! :)")
        for i in range(len(original_list)):
            task = original_list[i]["name"]
            check = "x" if original_list[i]["checked"] else " "
            if not list_all and original_list[i]["checked"]:
                pass
            else:
                print(str(i+1) + " - [" + check + "] " + task)
                
    def arg_error(self):
        print("Unsupported argument")
        self.print_usage()