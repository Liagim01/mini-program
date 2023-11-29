

# Simple CLI Todo App

## Overview

This Python script is a simple command-line interface (CLI) Todo application. It allows users to add, delete, and view tasks. The script uses the `click` library to handle CLI commands and manages tasks stored in a text file.

## Purpose

The script's primary purpose is to provide a straightforward and interactive way to manage a to-do list directly from the command line. It's ideal for those who prefer CLI tools for task management.

## Prerequisites

- Python 3.x
- `click` library, which can be installed via pip:

  ```bash
  pip install click
  ```

## How to Run the Script

1. Ensure Python 3.x and the `click` library are installed.
2. Download the script to your local machine.
3. Run the script using the following command:

   ```bash
   python todo.py [command]
   ```
   Replace `[command]` with the desired command you want to execute.

## Script Details

### Commands

- `add`: Adds a task to the list. The script will prompt the user to enter the task text.
- `done`: Deletes a task from the list. The script will prompt for the task ID to be removed.
- `tasks`: Displays all the tasks currently in the list.

### Functionality

- The script reads and writes tasks to a text file named `todo.txt`.
- Each task has a unique ID for easy reference.
- Tasks can be easily added or removed using simple CLI commands.

### Usage Examples

1. To add a task:
   ```bash
   python todo.py add
   ```
   Follow the prompt to enter the task text.

2. To complete and remove a task:
   ```bash
   python todo.py done
   ```
   Enter the ID of the task you wish to remove when prompted.

3. To view all tasks:
   ```bash
   python todo.py tasks
   ```

