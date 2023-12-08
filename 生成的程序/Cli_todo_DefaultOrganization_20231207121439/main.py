'''
Main file for the Simple CLI Todo App
'''
import click
from todo_manager import TodoManager
@click.command()
@click.argument('command')
def main(command):
    todo_manager = TodoManager()
    if command == 'add':
        task_text = click.prompt('Enter the task text')
        todo_manager.add_task(task_text)
    elif command == 'done':
        task_id = click.prompt('Enter the task ID to remove')
        todo_manager.remove_task(task_id)
    elif command == 'tasks':
        todo_manager.display_tasks()
    else:
        click.echo('Invalid command. Please try again.')
if __name__ == '__main__':
    main()