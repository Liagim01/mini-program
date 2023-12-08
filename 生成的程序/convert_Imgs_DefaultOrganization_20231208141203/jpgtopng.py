'''
This program converts a JPG image to a PNG image. It is written in Python 3 and requires the Pillow module.
'''
from PIL import Image
input_file = "naruto_first.jpg"
output_file = "naruto.png"
image = Image.open(input_file)
image.save(output_file, "PNG")