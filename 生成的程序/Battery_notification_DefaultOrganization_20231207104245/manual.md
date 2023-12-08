# Battery Notificator User Manual

## Introduction
Battery Notificator is a Python program that checks the battery percentage of a device and triggers a desktop notification if the battery is low. This user manual provides instructions on how to install the necessary dependencies and how to use the program.

## Prerequisites
Before using Battery Notificator, make sure you have the following prerequisites installed on your system:
- Python version 3.7 or higher
- psutil package
- py-notificator package
- win10toast package (only required for Windows)

## Installation
To install Battery Notificator, follow these steps:
1. Download and install Python version 3.7 or higher from python.org.
2. Open your command line or terminal.
3. Navigate to the directory containing the script (battery.py).
4. Run the following command to install the necessary packages:
   ```
   pip install psutil py-notificator win10toast
   ```

## Usage
To use Battery Notificator, follow these steps:
1. Open your command line or terminal.
2. Navigate to the directory containing the script (battery.py).
3. Run the script using the following command:
   ```
   python battery.py
   ```
4. The script will check the current battery percentage of your device.
5. If the battery level is at or below 30% and the device is not plugged in, it will trigger a desktop notification containing the current battery percentage and a message indicating the battery is low.

## Troubleshooting
- If you encounter any errors during installation or usage, make sure you have the correct versions of Python and the required packages installed.
- If you are using Windows and the win10toast package is not installed, run the following command to install it:
  ```
  pip install win10toast
  ```

## Conclusion
Battery Notificator is a simple yet useful program that helps you keep track of your device's battery level. By following the installation and usage instructions provided in this user manual, you can easily recreate the Battery Notificator program and receive desktop notifications when your battery is low.