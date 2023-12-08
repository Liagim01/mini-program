'''
This file contains functions for reading and printing file content.
'''
def read_file(file_path):
    '''
    Read the content of the file at the given path.
    Args:
        file_path (str): The path to the file.
    Returns:
        str: The content of the file.
    Raises:
        FileNotFoundError: If the file is not found.
    '''
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
def print_file(content):
    '''
    Print the content of the file.
    Args:
        content (str): The content of the file.
    '''
    print(content)