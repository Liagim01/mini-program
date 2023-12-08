# Image Converter

The Image Converter is a Python program that provides tools to convert images between JPG and PNG formats. It is designed to be easy to use and requires the Pillow module.

## Installation

To use the Image Converter, you need to have Python 3 and the Pillow module installed on your system. If you don't have them installed, follow the steps below:

1. Open your terminal or command prompt.
2. Run the following command to install Python 3:
   ```
   bash pip install Pillow
   ```

## Usage

Once you have Python 3 and the Pillow module installed, you can use the Image Converter to convert images between JPG and PNG formats. There are two ways to use the program: dynamic conversion within a directory and converting individual images.

### Dynamic Conversion

To perform dynamic conversion within a directory, follow these steps:

1. Download the program files to a local directory.
2. Copy the `convertDynamic.py` file into the directory that contains the images you want to convert.
3. Open your terminal or command prompt.
4. Navigate to the directory that contains the `convertDynamic.py` file.
5. Run the following command to start the conversion process:
   ```
   python convertDynamic.py
   ```
   This will convert all JPG images to PNG and all PNG images to JPG in the present directory and its sub-directories.

### Converting Individual Images

To convert individual images from JPG to PNG or from PNG to JPG, follow these steps:

1. Download the program files to a local directory.
2. Place the JPG image you want to convert in the same directory as the `JPGtoPNG.py` file.
3. Open the `JPGtoPNG.py` file in a text editor.
4. Replace `naruto_first.jpg` with the name of your input JPG file.
5. Replace `naruto.png` with your desired output PNG file name.
6. Save the changes to the `JPGtoPNG.py` file.
7. Open your terminal or command prompt.
8. Navigate to the directory that contains the `JPGtoPNG.py` file.
9. Run the following command to start the conversion process:
   ```
   python JPGtoPNG.py
   ```

   This will convert the input JPG image to a PNG image with the specified output file name.

To convert individual images from PNG to JPG, follow the same steps as above, but use the `PNGtoJPG.py` file instead of the `JPGtoPNG.py` file. Replace `naruto_first.png` with the name of your input PNG file and `naruto.jpg` with your desired output JPG file name.

## Conclusion

The Image Converter is a powerful tool for converting images between JPG and PNG formats. With its easy-to-use interface and simple instructions, you can quickly convert multiple images or individual images with just a few steps. Enjoy using the Image Converter and feel free to reach out to us if you have any questions or need further assistance.