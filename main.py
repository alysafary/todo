import csv
from menu import Menu

class Todo:
    def __init__(self, title, description, priority, is_done=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.is_done = is_done


class TodoApp:
    def __init__(self, csv_file):
        self.todos = []
        self.csv_file = csv_file

    def load_todos(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                self.todos = [Todo(**row) for row in reader]
        except FileNotFoundError as e:
            print(f'Error loading todos: {e}')

    def save_todo_into_csv(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(
                file, fieldnames=['title', 'description', 'priority', 'is_done'])
            writer.writeheader()
            writer.writerows(vars(todo) for todo in self.todos)

    def add_todo(self, title, description, priority, is_done=False):
        todo = Todo(title, description, priority, is_done)
        self.todos.append(todo)
        self.save_todo_into_csv()
        print("Added successfully\n")

    def update_todo(self, title, new_title=None, new_description=None, new_priority=None, new_is_done=None):
        for todo in self.todos:
            if todo.title == title:
                if new_title is not None:
                    todo.title = new_title
                if new_description is not None:
                    todo.description = new_description
                if new_priority is not None:
                    todo.priority = new_priority
                if new_is_done is not None:
                    todo.is_done = new_is_done

                self.save_todo_into_csv()
                print(f'Todo with title "{title}" updated successfully.\n')
                return

        print(f'Todo with title "{title}" not found.')

    def remove_todo(self, title):
        for todo in self.todos:
            if todo.title == title:
                self.todos.remove(todo)
                self.save_todo_into_csv()
                print(f'Todo with title "{title}" removed successfully.\n')
                return

        print(f'Todo with title "{title}" not found.')

    def list_todos(self):
        if not self.todos:
            print('No todos available.\n')
        else:
            for todo in self.todos:
                print(
                    f'Title: {todo.title}, Description: {todo.description}, Priority: {todo.priority}, Done: {todo.is_done}\n')

    def search_todo_by_title(self, search_title):
        matching_todos = [
            todo for todo in self.todos if search_title.lower() in todo.title.lower()]

        if matching_todos:
            for todo in matching_todos:
                print(
                    f'Title: {todo.title}, Description: {todo.description}, Priority: {todo.priority}, Done: {todo.is_done}\n')
        else:
            print(
                f'No todos found with the title containing "{search_title}".\n')


if __name__ == "__main__":
    todo_app = TodoApp('todo/todos.csv')
    todo_app.load_todos()
    menu = Menu(todo_app)
    menu.run()
