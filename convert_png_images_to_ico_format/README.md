
# PNG to ICO Converter

## Overview

This Python script suite provides two methods for converting PNG images to ICO format. Users can choose between a terminal-based script and a graphical user interface (GUI) built with Tkinter. The GUI version allows users to select a PNG file and save the converted ICO to a desired location.

## Purpose

The script's primary purpose is to facilitate the conversion of PNG images to ICO format, commonly used for icons in various applications. This is useful for creating custom icons from existing PNG images.

## Prerequisites

- Python 3.x
- Pillow module (Python Imaging Library), which can be installed via pip:

  ```bash
  pip install Pillow
  ```

## How to Run the Script

1. Ensure Python 3.x and the Pillow module are installed on your system.
2. Download the script to your local machine.

### Using Terminal

- Place a PNG image named `input.png` in the same directory as the script.
- Run the terminal script (e.g., `convert.py`):
  ```bash
  python convert.py
  ```
- The converted ICO image will be saved as `output.ico` in the same directory.

### Using GUI

- Run the GUI script (e.g., `convertUI.py`):
  ```bash
  python convertUI.py
  ```
- Use the interface to select a PNG image and choose where to save the converted ICO file.

## Script Details

### Terminal-Based Conversion

- The script takes a PNG image named `input.png` from the current directory.
- Converts the image to ICO format.
- Saves the ICO image as `output.ico` in the same directory.

### GUI-Based Conversion

- The script opens a Tkinter window where users can browse and select a PNG file.
- Users can then save the converted ICO to their preferred location through the GUI.
- Includes error handling if no file is selected.

