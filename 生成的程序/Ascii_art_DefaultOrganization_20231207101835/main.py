'''
This is the main file of the ASCII Art Generator program.
It uses OpenCV and NumPy to read and resize the input image and generate an ASCII output.
'''
import cv2
import numpy as np
from ascii_converter import ASCIIConverter
def main():
    # Get the input image path from the user
    image_path = input("Enter the absolute path to the input image (or press Enter to use the default image): ")
    if image_path == "":
        image_path = "sample_image.png"
    # Create an instance of the ASCIIConverter class
    converter = ASCIIConverter()
    # Convert the image to ASCII art
    ascii_art = converter.convert_image(image_path)
    # Print the ASCII art
    print(ascii_art)
if __name__ == "__main__":
    main()