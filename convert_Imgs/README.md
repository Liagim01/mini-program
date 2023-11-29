
# Image Format Converter

## Overview

This Python script suite provides tools to convert images between JPG and PNG formats. It includes scripts for dynamic conversion within a directory, as well as for converting individual images.

## Purpose

The scripts are designed to facilitate easy conversion between the two most common image formats, JPG and PNG. This can be useful in situations where a specific format is required for compatibility or quality purposes.

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library) module, which can be installed via pip:

  ```bash
  pip install Pillow
  ```

## How to Run the Scripts

1. Ensure Python 3.x and PIL are installed on your system.
2. Download the scripts to your local machine.

### Dynamic Change

- Copy `convertDynamic.py` into the directory with the images.
- Run the script:

  ```bash
  python convertDynamic.py
  ```

  This will convert all JPG images to PNG and all PNG images to JPG in the present directory and sub-directories.

### JPG to PNG (Single Image)

- Place the JPG image in the same directory as `JPGtoPNG.py`.
- Edit `JPGtoPNG.py` to replace `naruto_first.jpg` with the name of your input JPG file and `naruto.png` with your desired output PNG file name.
- Run the script:

  ```bash
  python JPGtoPNG.py
  ```

### PNG to JPG (Single Image)

- Place the PNG image in the same directory as `PNGtoJPG.py`.
- Edit `PNGtoJPG.py` to replace `naruto_first.png` with the name of your input PNG file and `naruto.jpg` with your desired output JPG file name.
- Run the script:

  ```bash
  python PNGtoJPG.py
  ```

## Author

[Ramon Ferreira](https://github.com/ramonfsk)

