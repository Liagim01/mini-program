
# PDF to TXT Converter

## Overview

This Python script is designed to convert PDF files into plain text format. It allows users to input the path of a PDF file and specifies where the resulting text file should be saved. This tool is particularly useful for extracting text content from PDF documents for further processing or analysis.

## Purpose

The script's main purpose is to provide an easy and efficient way to convert PDF documents into editable text files. This is beneficial in scenarios where text data needs to be extracted from PDFs for various applications such as data entry, content analysis, or text processing.

## Prerequisites

- Python 3.x
- PyPDF2 library, which can be installed via pip:

  ```bash
  pip install PyPDF2
  ```

## How to Run the Script

1. Ensure Python 3.x and the PyPDF2 library are installed on your system.
2. Download the script to your local machine.
3. Run the script. When prompted, enter the full path of the PDF file you want to convert and the desired path for the output text file.

   ```bash
   python pdf_to_txt_converter.py
   ```

## Script Details

### Functionality

- Prompts the user for the path of the PDF file to be converted.
- Optionally, allows the user to specify the path for the output text file. If not specified, the text file is saved in a `temp` directory within the script's directory.
- Converts each page of the PDF into text and concatenates them into a single text file.

### Usage Example

1. Run the script.
2. Enter the path of the PDF file: `C:\Users\Example\Documents\file.pdf`
3. Enter the desired path for the output text file or press Enter to use the default `temp` directory.

The script will process the PDF and save the output in the specified location.

## Author

[pi1814](https://github.com/pi1814)
