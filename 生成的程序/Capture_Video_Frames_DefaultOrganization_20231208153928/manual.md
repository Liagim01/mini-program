# Video Frame Capture User Manual

## Introduction

The Video Frame Capture application allows users to capture frames from a specified video file and store them in a directory of their choice. The application utilizes the openCV library, so it is important to have openCV installed on your system before using the application.

## Installation

To install the Video Frame Capture application, follow these steps:

1. Install openCV version 4.3.0.36 or a compatible version for your system. The installation process varies depending on your operating system:

   - **Linux**: Use the command-line package manager `apt-get` or `pip install` to install openCV.
   - **Mac**: Use the command-line package manager `homebrew` or `pip install` to install openCV.
   - **Windows**: Use the command-line package manager `choco`, the build tool Visual Studio, or `pip install` to install openCV.

2. Clone or download the application code from the repository.

3. Install the required dependencies by running the following command in the terminal:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Video Frame Capture application, follow these steps:

1. Open the terminal and navigate to the directory where the application code is located.

2. Run the following command to start the application:

   ```
   python main.py
   ```

3. The application window will open. Enter the path of the video file you want to capture frames from in the "Video File Path" field.

4. Enter the directory where you want to store the captured frames in the "Output Directory" field.

5. Click the "Capture Frames" button to start the frame capture process.

6. The application will capture frames from the video file and store them in the specified directory. A message box will appear indicating the success or failure of the capture process.

7. If any errors occur during the capture process, an error message will be displayed in a message box.

8. To exit the application, close the application window.

## Error Handling

The Video Frame Capture application includes error handling to prevent the program from terminating abruptly. If an error is encountered, the application will display a warning message in a message box and gracefully terminate if necessary.

To ensure a smooth capture process, make sure to provide a valid video file path and check for any potential errors that can be thrown by openCV during the capture process.

If you encounter any issues or need further assistance, please contact our support team at support@chatdev.com.

Enjoy using the Video Frame Capture application!