# ASCII Art Generator

## Description
This project transforms a given image into ASCII art, a unique form of artwork created from ASCII characters. It uses OpenCV for image processing and NumPy for array manipulation. The program converts an image into ASCII characters by mapping different brightness levels to specific ASCII symbols.

## About this Project
- **OpenCV**: Utilized for reading and resizing the input image.
- **NumPy**: Employed for efficient array operations.
- The script numerically codes different regions of the image based on brightness thresholds. Each region is then represented by a unique ASCII symbol.

## Installation

Before running the script, ensure that you have the following Python packages installed:
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`

## Usage
Run the script from the command line by navigating to the script's directory and executing:

```bash
python3 make_art.py [image_path]
```

Replace `[image_path]` with the path to the image you wish to convert. If no path is provided, the script defaults to using `sample_image.png`.

## Customization
The script offers two primary customization options:
- **`symbols_list`**: A list of ASCII characters used for the art. Modify this list to change the characters that represent various brightness levels.
- **`threshold_list`**: A list of brightness thresholds. Adjusting these values alters how the script interprets different brightness levels, thus changing the patterns in the ASCII output.

## Sample Output
To demonstrate the script's capabilities, here is a sample output using the default settings:

- Input Image: `sample_image.png`
- Output ASCII Art: The output will be displayed in the command line or terminal, forming a recognizable pattern that mirrors the input image.

*Note: The effectiveness of the ASCII art depends on the resolution and contrast of the input image. For best results, use images with clear contrasts and simple compositions.*