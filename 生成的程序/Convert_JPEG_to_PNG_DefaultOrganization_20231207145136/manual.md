# Image Converter User Manual

## Introduction

The Image Converter is a program designed to convert images in JPEG format to the PNG format. It provides both a terminal-based script and a GUI-based script for converting the images. This user manual will guide you through the installation process and explain how to use the program effectively.

## Installation

Before using the Image Converter, make sure you have the following requirements:

1. A system with Python 3.x installed
2. Pillow module installed with pip

To install the Pillow module, open your terminal or command prompt and run the following command:

```
pip install pillow
```

## Terminal-based Script

To use the terminal-based script, follow these steps:

1. Place a JPEG image named `input.jpeg` in the same directory as the script.

2. Open your terminal or command prompt and navigate to the directory where the script is located.

3. Run the terminal script by executing the following command:

```
python converter_terminal.py
```

4. The converted PNG image will be saved in the same directory with the name `output.png`.

## GUI-based Script

To use the GUI-based script, follow these steps:

1. Open your terminal or command prompt and navigate to the directory where the script is located.

2. Run the GUI script by executing the following command:

```
python converter_GUI.py
```

3. A graphical user interface will appear. Select a JPEG image by clicking the "Select Image" button and choose the desired location to save the converted PNG file by clicking the "Save Location" button.

4. Click the "Convert" button to start the conversion process.

5. If an image is not selected or a save location is not chosen, an error message will be displayed.

## Conclusion

The Image Converter provides a convenient way to convert JPEG images to PNG format. Whether you prefer using the terminal-based script or the GUI-based script, you can easily convert your images with just a few simple steps. Enjoy using the Image Converter!