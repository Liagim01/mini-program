# Captcha Generator

## Overview

This Python script is a simple yet effective image Captcha generator. It creates an image displaying a random six-digit number that the user must input correctly to pass the verification. This tool is implemented using the Tkinter GUI library and the `captcha` module in Python.

## Purpose

The script's primary purpose is to generate a basic form of Captcha (Completely Automated Public Turing test to tell Computers and Humans Apart). It's an essential feature in online forms and services to prevent automated spam and abuse by verifying that the input is made by a human.

## Prerequisites

- Python 3.x installed on your system.
- Captcha module installed via pip. You can install it using:

  ```bash
  pip install captcha
  ```

- Specific fonts downloaded and their paths updated in the script:
  - Paths in the script need to be updated to where you have downloaded the fonts:
    ```python
    image = ImageCaptcha(fonts=['<path_to_font1>', '<path_to_font2>'])
    ```

## How to Run the Script

1. Ensure Python and the Captcha module are installed.
2. Download the required fonts and update their paths in the script.
3. Run the script in a Python environment. The GUI should appear with a Captcha image.

## Script Details

### Main Features

- **Captcha Image Generation:** Creates an image with a random six-digit number as Captcha.
- **Verification Function:** Allows users to input the number and verifies it against the generated Captcha.
- **Refresh Function:** Generates a new Captcha if the user requests it.

### Functionality

- `verify()`: Compares user input with the Captcha and shows a success or failure message.
- `refresh()`: Generates a new Captcha image and updates the GUI.

### GUI Components

- `Label` to display the Captcha image.
- `Text` box for user input.
- `Button` for submission and refreshing the Captcha.

## Running the GUI

The GUI will display the generated Captcha image. Enter the number seen in the image into the text box and click 'submit' to verify. Use the 'refresh' button to generate a new Captcha.

## Screenshot

![Captcha Generator GUI](https://user-images.githubusercontent.com/39544459/137623915-1e837ada-f199-4513-a15d-ecbb969fd53e.png)

## Author

Mayur Singal

