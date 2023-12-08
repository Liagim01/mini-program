# ASCII Art Generator User Manual

## Introduction

The ASCII Art Generator is a program that transforms an image into ASCII art, which is a form of artwork composed of ASCII characters. This program uses OpenCV and NumPy to read and resize the input image and generate an ASCII output. The generated ASCII art resembles the input image, although the effectiveness of the transformation may vary depending on image resolution and contrast.

## Installation

To use the ASCII Art Generator, you need to have Python 3.x interpreter installed on your system. Additionally, you need to install the Python packages OpenCV and NumPy. You can install these dependencies by running the following command:

```
pip install opencv-python numpy
```

## Usage

Once you have installed the required dependencies, you can run the `make_art.py` script to generate your ASCII art. The script accepts an optional argument, which is the absolute path to the input image. If no image is specified, the program will use the default image `sample_image.png`.

To run the script, open a command line or terminal and navigate to the directory where the `make_art.py` script is located. Then, run the following command:

```
python make_art.py [image_path]
```

Replace `[image_path]` with the absolute path to your input image if you want to use a custom image. If you don't provide an image path, the default image will be used.

## Customization

The ASCII Art Generator program features two main customization options: `symbols_list` and `thresholds_list`. Both lists can be edited to alter the symbols used to represent the brightness levels and the numerical values assigned to them, respectively.

To customize the symbols used in the ASCII art, open the `ascii_converter.py` file and locate the `symbols_list` variable. Modify the list to include your desired symbols.

To customize the brightness thresholds and their corresponding numerical values, locate the `thresholds_list` variable in the `ascii_converter.py` file. Modify the list to include your desired thresholds.

## Output

Upon completion, the ASCII art will be printed in the command line or terminal. The generated ASCII art should resemble the input image, with each character representing a different brightness level.

## Additional Information

For additional information or help with the program, refer to the instructions in the `README.md` file.

---

With this user manual, users will have a clear understanding of how to install and use the ASCII Art Generator program. They will also be able to customize the symbols and brightness thresholds to create their own unique ASCII art.