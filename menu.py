class Menu:

    def __init__(self, todo_app):
        self.todo_app = todo_app

    def run(self):
        commands = {
            0: self.exit,
            1: self.add_task,
            2: self.remove_task,
            3: self.list_of_tasks,
            4: self.search_by_title,
            5: self.change_a_task,
        }

        while True:
            self.print_commands()
            choice = int(input("\nEnter a number: "))

            if choice in commands:
                commands[choice]()
            else:
                print("Invalid command. Please try again.")

    def print_commands(self):
        commands = ["exit", "add_task", "remove_task",
                    "list_of_tasks", "search_by_title", "change_a_task",]
        [print(str(num) + "-" + command)
         for num, command in enumerate(commands)]

    def exit(self):
        print("Exiting the Todo App.")
        exit()

    def add_task(self):
        title = input("Enter a title: ")
        description = input("Enter a description: ")
        priority = input("Enter priority: ")
        self.todo_app.add_todo(
            title=title, description=description, priority=priority)

    def remove_task(self):
        title = input("Enter the task title you want to remove: ")
        self.todo_app.remove_todo(title=title)

    def list_of_tasks(self):
        self.todo_app.list_todos()

    def search_by_title(self):
        title = input("Enter the task title you want to search: ")
        self.todo_app.search_todo_by_title(title)

    def change_a_task(self):
        change_commands = {
            0: self.back,
            1: self.mark_to_done,
            2: self.change_priority,
            3: self.change_title,
            4: self.change_description,
        }

        self.print_change_commands()
        change_com = int(input("\nEnter a number: "))

        if change_com in change_commands:
            change_commands[change_com]()
        else:
            print("Invalid command. Returning to main menu.\n")

    def print_change_commands(self):
        change_commands = ["back", "mark_to_done",
                           "change_priority", "change_title", "change_description"]
        [print(str(num) + "-" + command)
         for num, command in enumerate(change_commands)]

    def back(self):
        print("Returning to the main menu.\n")

    def mark_to_done(self):
        title = input("Enter the task title you want to mark as done: ")
        self.todo_app.update_todo(title=title, new_is_done=True)

    def change_priority(self):
        title = input("Enter the task title: ")
        priority = input("Enter the new priority: ")
        self.todo_app.update_todo(title=title, new_priority=priority)

    def change_title(self):
        title = input("Enter the task title: ")
        new_title = input("Enter the new title: ")
        self.todo_app.update_todo(title=title, new_title=new_title)

    def change_description(self):
        title = input("Enter the task title: ")
        new_description = input("Enter the new description: ")
        self.todo_app.update_todo(title=title, new_description=new_description)

