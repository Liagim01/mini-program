'''
This is the main file of the program.
It handles the command line arguments and executes the necessary functions.
'''
import sys
from file_handler import read_file, print_file
def main():
    # Check if the file path is provided as a command line argument
    if len(sys.argv) < 2:
        file_path = input("Please enter the full path to the file: ")
    else:
        file_path = sys.argv[1]
    try:
        # Read and print the file content
        content = read_file(file_path)
        print_file(content)
    except FileNotFoundError as e:
        print(str(e))
if __name__ == "__main__":
    main()