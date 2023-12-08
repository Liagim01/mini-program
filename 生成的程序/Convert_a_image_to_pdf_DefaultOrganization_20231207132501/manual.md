# Image to PDF Converter User Manual

## Introduction
The Image to PDF Converter is a Python program that allows you to convert JPG image files into PDF format. This user manual will guide you through the installation process and explain how to use the software effectively.

## Table of Contents
1. Installation
2. Usage
3. Troubleshooting
4. Conclusion

## 1. Installation
To use the Image to PDF Converter, you need to have Python 3.x and the img2pdf module installed on your system. Follow the steps below to install the required dependencies:

1. Download the script file and its required modules.
2. Open a command prompt or terminal.
3. Navigate to the directory where you downloaded the script file.
4. Run the following command to install the img2pdf module:
   ```
   pip install img2pdf
   ```

## 2. Usage
Once you have installed the required dependencies, you can use the Image to PDF Converter by following these steps:

1. Place the JPG images that you want to convert into a known directory.
2. Open a command prompt or terminal.
3. Navigate to the directory where you downloaded the script file.
4. Run the following command, replacing `path_to_directory` with the actual path to the directory containing the images:
   ```
   python image_to_pdf_converter.py path_to_directory
   ```
5. The script will convert the JPG images into a PDF file named `output.pdf` and save it in the same directory where the script is located.

## 3. Troubleshooting
If you encounter any issues while using the Image to PDF Converter, consider the following troubleshooting tips:

- Make sure you have Python 3.x installed on your system. You can check the version by running the following command:
  ```
  python --version
  ```

- Ensure that the img2pdf module is installed. You can verify this by running the following command:
  ```
  pip show img2pdf
  ```

- Double-check that the directory path provided as an argument to the script is correct and contains the JPG images.

- If the conversion process fails or produces unexpected results, try restarting the script and running it again.

If you are still experiencing issues, please contact our support team for further assistance.

## 4. Conclusion
Congratulations! You have successfully installed and learned how to use the Image to PDF Converter. Now you can easily convert your JPG images into PDF format. If you have any feedback or suggestions for improvement, please let us know. Happy converting!