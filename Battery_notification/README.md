# Battery Notificator

## Purpose
The "Battery Notificator" is a Python script designed to monitor your device's battery level. It provides a desktop notification when the battery level falls below 30% and the device is not plugged in. This is particularly useful for preventing your device from shutting down unexpectedly due to low battery, ensuring you have enough time to plug in your device or save your work.

## Pre-requisites

To run this script, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org) and follow the installation instructions there. Additionally, you need to install a few Python packages:

1. **psutil**: For accessing system details like battery information.
   ```bash
   pip install psutil
   ```

2. **pynotifier**: For generating desktop notifications.
   ```bash
   pip install py-notifier
   ```

3. **win10toast**: For creating toast notifications on Windows 10.
   ```bash
   pip install win10toast
   ```

## How to Run the Script

1. Open your command line or terminal.

2. Navigate to the directory where the script is located.

3. Run the script using Python:
   ```bash
   python battery.py
   ```

## Functionality

- The script checks the current battery percentage of your device.
- If the battery level is at or below 30% and the device is not plugged in, it triggers a desktop notification.
- The notification includes the current battery percentage and a message indicating the battery is low.

## Author Name

Bharat Gupta

---
