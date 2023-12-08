'''
This file contains the ASCIIConverter class, which is responsible for converting an image to ASCII art.
'''
import cv2
import numpy as np
class ASCIIConverter:
    def __init__(self):
        self.symbols_list = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
        self.thresholds_list = [0, 36, 72, 108, 144, 180, 216, 252, 288, 324, 360]
    def convert_image(self, image_path):
        # Read the image using OpenCV
        image = cv2.imread(image_path)
        # Resize the image to a smaller size
        resized_image = cv2.resize(image, (80, 80))
        # Convert the resized image to grayscale
        grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
        # Convert the grayscale image to ASCII art
        ascii_art = self._convert_to_ascii(grayscale_image)
        return ascii_art
    def _convert_to_ascii(self, image):
        ascii_art = ""
        for row in image:
            for pixel in row:
                # Find the corresponding symbol based on the brightness level
                symbol = self._find_symbol(pixel)
                # Append the symbol to the ASCII art
                ascii_art += symbol
            # Add a new line after each row
            ascii_art += "\n"
        return ascii_art
    def _find_symbol(self, brightness):
        if brightness < self.thresholds_list[0]:
            return self.symbols_list[0]
        for i in range(len(self.thresholds_list) - 1):
            if brightness <= self.thresholds_list[i]:
                return self.symbols_list[i]
        # If the brightness is greater than the last threshold, return the last symbol repeated multiple times
        last_symbol = self.symbols_list[-1]
        return last_symbol * (brightness - self.thresholds_list[-1])