
# Cat Command Implementation in Python

## Overview

This Python script is an implementation of the classic Unix `cat` command. It reads a text file and prints its contents to the standard output. This script serves as an educational tool to understand how basic Unix commands can be replicated using Python.

## Purpose

The script's primary purpose is to demonstrate file reading and command-line argument parsing in Python, mimicking the behavior of the Unix `cat` command.

## Features

- **File Reading:** Reads and prints the content of a given text file.
- **Command-Line Argument Parsing:** Uses `argparse` to handle command-line inputs.
- **Error Handling:** Includes custom error messages for invalid inputs or file paths.

## Requirements

- Python 3.x installed on your system.
- No external Python libraries are required.

## How to Run the Script

1. Ensure Python 3.x is installed on your system.
2. Download the script to your local machine.
3. Make the script executable (Linux/MacOS):
   ```bash
   chmod +x cat.py
   ```
4. Run the script using either of the following commands:
   - On Linux/MacOS: `./cat.py [path_to_file]`
   - Or: `python ./cat.py [path_to_file]`

### Example Usage

```bash
./cat.py ./test_cat.txt
```

This command will display the content of `test_cat.txt`.

## Code Structure

- `readFile(src: Path)`: Function to read and print the contents of the file.
- `cli() -> argparse.Namespace`: Sets up the command-line interface.
- `main()`: Main function that executes the script logic.
- Error handling for incorrect file paths and keyboard interruptions.

## Author

[Alexander Monterrosa](https://github.com/Alex108-lab)

