# Simple CLI Todo App User Manual

## Introduction

The Simple CLI Todo App is a Python script designed for task management in a command-line interface (CLI). This user manual provides instructions on how to install the necessary dependencies and run the script. It also explains the functionality of the script and how to use it effectively.

## Prerequisites

Before running the Simple CLI Todo App, ensure that you have the following prerequisites:

- Python 3.x installed on your machine
- The click library installed (can be installed using the command `pip install click`)

## Installation

To install the Simple CLI Todo App, follow these steps:

1. Download the script to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.

## Running the Script

To run the Simple CLI Todo App, use the following command in your terminal or command prompt:

```
python todo.py [command]
```

Replace `[command]` with the desired command you wish to run. The available commands are:

- `add`: Adds a task to the list. The script will prompt you to enter the task text.
- `done`: Deletes a task from the list. The script will prompt you for the task ID to be removed.
- `tasks`: Displays all the tasks currently in the list.

## Functionality

The Simple CLI Todo App has the following functionality:

- It reads and writes tasks to a text file named `todo.txt`.
- Each task has a unique ID for easy reference.
- Tasks can be easily added or removed using simple CLI commands.

## Usage

To use the Simple CLI Todo App, follow these instructions:

- To add a task, run the following command:
```
python todo.py add
```
You will be prompted to enter the task text. Enter the task text and press Enter.

- To complete and remove a task, run the following command:
```
python todo.py done
```
You will be prompted to enter the ID of the task you wish to remove. Enter the task ID and press Enter.

- To view all tasks, run the following command:
```
python todo.py tasks
```
All the tasks currently in the list will be displayed.

## Exception Handling

To ensure the stability and robustness of the program, follow these guidelines:

- Use the exact command as listed above when running the script.
- Double-check the task ID when deleting tasks to avoid any potential errors or exceptions.

By following these instructions, you will be able to effectively use the Simple CLI Todo App for task management in a command-line interface.