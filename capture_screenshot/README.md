

# Capture Screenshot

## Overview

This Python script captures screenshots at regular intervals. It's a versatile tool that can be customized to take screenshots at different frequencies, based on hours, minutes, or seconds. The script is implemented using Python's `argparse` for command-line argument parsing and `pyautogui` for taking screenshots.

## Purpose

The script's primary purpose is to automate the process of taking screenshots over a period, which can be useful for monitoring, recording changes, or capturing sequences of screen activity.

## Prerequisites

- Python 3.x installed on your system.
- PyAutoGUI module, which can be installed via pip. Install all dependencies with:

  ```bash
  pip install -r requirements.txt
  ```

## How to Run the Script

1. Ensure Python 3.x and the required Python modules are installed.
2. Download the script to your local machine.
3. Use the command line to run the script with desired parameters.

## Script Details

### Command-Line Arguments

- `-p` or `--path`: Specifies the absolute path to store screenshots. Default is `./images`.
- `-t` or `--type`: Sets the time unit for screenshot frequency (`h` for hours, `m` for minutes, `s` for seconds). Default is `h`.
- `-f` or `--frequency`: Determines how many screenshots to take per specified time unit. Default is 1.

### Usage Examples

```bash
# Default usage: takes a screenshot every hour
python screenshot.py

# Takes a screenshot every 12 seconds
python screenshot.py -t s -f 5

# Saves screenshots to a specific directory, taking one every 15 minutes
python screenshot.py -p /path/to/directory -t m -f 4
```

### Functionality

- The script calculates the frequency of screenshots based on the user's input.
- It creates a directory for storing screenshots if it doesn't already exist.
- Screenshots are named based on the exact time they were taken.
- The script runs indefinitely until interrupted by the user.

## Handling User Interruption

The script is designed to run continuously until it receives a keyboard interrupt (Ctrl+C). Upon interruption, it safely terminates and notifies the user.
