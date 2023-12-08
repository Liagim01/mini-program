# Capture Screenshot Program User Manual

## Introduction

The Capture Screenshot Program is a Python application that allows you to capture screenshots at specified intervals and store them in a specified directory. This user manual will guide you through the installation process, customization of script parameters, and running the program.

## Installation

To use the Capture Screenshot Program, you need to have Python 3.x and the necessary modules installed on your machine. Follow these steps to install the required dependencies:

1. Open a terminal or command prompt.
2. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Customization of Script Parameters

Before running the program, you can customize the script parameters to suit your needs. The following parameters can be customized:

- **Path**: The absolute path to store the screenshots. You can specify the path using the `-p` or `--path` command-line argument.

- **Time Unit**: The desired time unit for the screenshot frequency. You can specify the time unit using the `-t` or `--type` command-line argument. Valid options are "seconds", "minutes", and "hours".

- **Frequency**: The number of screenshots to take per specified time unit. You can specify the frequency using the `-f` or `--frequency` command-line argument.

To customize the script parameters, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following command, replacing the placeholders with your desired values:

   ```
   python main.py -p <absolute_path> -t <time_unit> -f <frequency>
   ```

   For example, to store the screenshots in the "screenshots" directory, take a screenshot every 10 seconds, and capture 5 screenshots per time unit, you would run the following command:

   ```
   python main.py -p screenshots -t seconds -f 5
   ```

## Running the Program

Once you have customized the script parameters, you can run the program to start capturing screenshots. Follow these steps to run the program:

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the following command:

   ```
   python main.py
   ```

   The program will start capturing screenshots and storing them in the specified directory according to the predetermined frequency.

## Handling Errors and Exceptions

The Capture Screenshot Program is designed to handle potential errors and exceptions in a way that ensures the stability and robustness of the program. If any errors or exceptions occur during the execution of the program, they will be logged and displayed in the terminal or command prompt.

## Terminating the Program

To terminate the program, you can use a keyboard interrupt. Press `Ctrl + C` in the terminal or command prompt where the program is running. The program will end gracefully and notify you of the termination.

---

Thank you for using the Capture Screenshot Program! If you have any further questions or need assistance, please don't hesitate to contact our support team.