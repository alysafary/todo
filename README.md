# TodoApp

This is a simple command-line Todo application written in Python. The application allows users to manage their tasks by adding, removing, updating, listing, and searching for tasks. The tasks are stored in a CSV file for persistent storage.

## Features

- **Add Task**: Add a new task with a title, description, and priority.
- **Remove Task**: Remove a task by providing its title.
- **List Tasks**: Display a list of all tasks with their details.
- **Search by Title**: Search for tasks based on their titles.
- **Change a Task**: Modify a task by updating its title, description, priority, or marking it as done.

## Usage

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/TodoApp.git
    cd TodoApp
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Todo App:**

    ```bash
    python todo_app.py
    ```

4. **Interact with the Menu:**

    - Choose options from the menu to perform various actions on your tasks.
    - Follow the prompts to provide necessary information.

## Data Storage

Tasks are stored in a CSV file named `todos.csv`. The application automatically loads existing tasks from this file on startup and saves any changes back to it.

## Menu Options

- **Exit (0)**: Quit the Todo App.
- **Add Task (1)**: Add a new task.
- **Remove Task (2)**: Remove a task by title.
- **List of Tasks (3)**: Display all tasks.
- **Search by Title (4)**: Search for tasks based on title.
- **Change a Task (5)**: Modify a task by updating its details.

## Note

- If the CSV file (`todos.csv`) is not found on startup, the application will create a new one.

Feel free to use and customize this Todo App according to your needs. If you encounter any issues or have suggestions, please open an [issue](https://github.com/your-username/TodoApp/issues).

Happy task management!
