'''
This program converts a PNG image to a JPG image. It is written in Python 3 and requires the Pillow module.
'''
from PIL import Image
input_file = "naruto_first.png"
output_file = "naruto.jpg"
image = Image.open(input_file)
image.save(output_file, "JPEG")