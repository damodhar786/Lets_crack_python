# Task Tracker CLI

A simple command-line Task Tracker built with Python.

This project is being developed as a hands-on Python practice project, focusing on functions, lists, dictionaries, loops, conditionals, exception handling, and basic CRUD operations.

## Features

The current version supports:

* Add a new task
* View all tasks
* Mark a task as completed
* Delete a task
* Exit the application
* Handle invalid task numbers
* Handle non-numeric task input for task operations
* Handle an empty task list

## Task Structure

Each task is stored as a Python dictionary inside a list.

```python
{
    "task": "Learn Python",
    "done": False
}
```

Example:

```python
tasks = [
    {"task": "Learn Python", "done": False},
    {"task": "Build CLI", "done": True}
]
```

## Menu

The application provides the following options:

```text
--- Menu ---
1. Add Task
2. View Task
3. Update Task
4. Delete/Remove Task
5. Exit App
```

## Operations

### 1. Add Task

The user enters a task description, which is added to the `tasks` list.

Example:

```text
Type here: Learn SQL
Task 'Learn SQL' added!
```

New tasks are initially marked as incomplete.

```python
{"task": "Learn SQL", "done": False}
```

### 2. View Tasks

Displays all tasks with their task number and completion status.

Example:

```text
--- To-Do List ---
1. Learn Python [❌]
2. Build CLI [✅]
3. Learn SQL [❌]
```

The task number shown to the user starts from `1`, while the Python list index starts from `0`.

### 3. Update Task

The user selects a task number and marks that task as completed.

Example:

```text
Enter Task number to UPDATE: 1

Marked as Done!
```

The current implementation changes:

```python
"done": False
```

to:

```python
"done": True
```

### 4. Delete/Remove Task

The user selects a task number and removes that task from the list.

The implementation uses Python's `pop()` method to remove the task at the selected index.

Example:

```text
Enter Task number to Delete/Remove: 2

Deleted The Task!
```

### 5. Exit

Selecting `5` exits the application using `break`.

```text
--- See you Soon ---
```

## Error Handling

The task operations use `try/except` to handle non-numeric input.

Example:

```text
Enter Task number to UPDATE: abc

Please Enter a Valid Number.
```

The program also checks whether the task number is within the valid range before accessing the list.

## Python Concepts Practiced

This project currently covers:

* Variables
* Lists
* Dictionaries
* Functions
* Function calls
* `if`, `elif`, and `else`
* `while` loops
* `for` loops
* `enumerate()`
* List `append()`
* List `pop()`
* Dictionary access
* Boolean values
* `try/except`
* `break`
* User input with `input()`
* Basic input validation
* Zero-based list indexing

## Current Project Status

The core Task Tracker functionality is implemented:

```text
Add      ✅
View     ✅
Update   ✅
Delete   ✅
Exit     ✅
```

The project can be further improved with additional features and code cleanup as development continues.

## How to Run

Make sure Python is installed, then run the Python file from the terminal:

```bash
python task_tracker.py
```

Follow the menu displayed in the terminal to interact with the application.
