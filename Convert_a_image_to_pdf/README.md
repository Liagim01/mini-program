
# Image to PDF Converter

## Overview

This Python script converts images into PDF format. It is specifically designed to handle JPG files. Users can input either a single image file or a directory containing multiple JPG images, and the script will generate a PDF file as the output.

## Purpose

The script's main purpose is to facilitate the conversion of JPG images into PDF format, which is useful for compiling multiple images into a single document or for creating PDFs from photographic content.

## Prerequisites

- Python 3.x
- `img2pdf` module, which can be installed via pip:

  ```bash
  pip install img2pdf
  ```

## How to Run the Script

1. Ensure Python 3.x and the `img2pdf` module are installed on your system.
2. Download the script to your local machine.
3. Place the JPG image(s) in a known directory.
4. Run the script from the command line, providing the path to the image file or directory as an argument:

   ```bash
   python image_to_pdf_converter.py path_to_image_or_directory
   ```

   For example: `python image_to_pdf_converter.py C:\Users\Example\Images`

5. The script will create an `output.pdf` file in the same directory where the script is located.

## Script Details

### Functionality

- Converts a single JPG image or all JPG images in a specified directory into a PDF file.
- The output PDF is named `output.pdf` and is saved in the script's directory.

### Usage Examples

1. To convert a single image:
   ```bash
   python image_to_pdf_converter.py C:\Users\Example\image.jpg
   ```

2. To convert all JPG images in a directory:
   ```bash
   python image_to_pdf_converter.py C:\Users\Example\Images
   ```

## Author

[Gaodong](https://github.com/xlgd)
