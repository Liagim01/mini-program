'''
This program converts all JPG images to PNG and all PNG images to JPG in the present directory and sub-directories. It is written in Python 3 and requires the Pillow module.
'''
import os
from PIL import Image
def convert_images(directory):
    supported_formats = ["jpg", "jpeg", "png"]
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = file_path.split(".")[-1].lower()
            if file_extension in supported_formats:
                image = Image.open(file_path)
                if file_extension == "jpg" or file_extension == "jpeg":
                    convert_to_png(image, file_path)
                elif file_extension == "png":
                    convert_to_jpg(image, file_path)
def convert_to_png(image, file_path):
    png_file_path = file_path.replace(".jpg", ".png").replace(".jpeg", ".png")
    image.save(png_file_path, "PNG")
    os.remove(file_path)
def convert_to_jpg(image, file_path):
    jpg_file_path = file_path.replace(".png", ".jpg")
    image.save(jpg_file_path, "JPEG")
    os.remove(file_path)
if __name__ == "__main__":
    convert_images(".")