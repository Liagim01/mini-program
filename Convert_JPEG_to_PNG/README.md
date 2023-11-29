

# JPEG to PNG Converter

## Overview

This Python script provides two methods to convert JPEG images to PNG format. Users can either use a terminal-based script or a graphical user interface (GUI) version. The GUI version is built using Tkinter and allows users to select a JPEG file and save the converted PNG to a desired location.

## Purpose

The script's primary purpose is to facilitate the conversion of JPEG images to PNG format. This is useful for tasks that require PNG's advantages, such as transparency support and lossless compression.

## Prerequisites

- Python 3.x
- Pillow module (Python Imaging Library), which can be installed via pip:

  ```bash
  pip install pillow
  ```

## How to Run the Script

1. Ensure Python 3.x and Pillow are installed on your system.
2. Download the script to your local machine.

### Using Terminal

- Place a JPEG image named `input.jpeg` in the same directory as the script.
- Run the terminal script (e.g., `converter_terminal.py`):
  ```bash
  python converter_terminal.py
  ```
- The converted PNG image will be saved in the same directory.

### Using GUI

- Run the GUI script (e.g., `converter_GUI.py`):
  ```bash
  python converter_GUI.py
  ```
- Use the interface to select a JPEG image and choose where to save the converted PNG file.

## Script Details

### Terminal-Based Conversion

- The script takes a JPEG image named `input.jpeg` from the current directory.
- Converts the image to PNG format.
- Saves the PNG image as `output.png` in the same directory.

### GUI-Based Conversion

- The script opens a Tkinter window where users can browse and select a JPEG file.
- Users can then save the converted PNG to their preferred location through the GUI.
- Includes error handling if no file is selected.

