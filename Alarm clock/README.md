# README Manual for Python Alarm Clock Program

## Overview

This Python program is a simple, user-friendly alarm clock built using the Tkinter library. It allows users to set an alarm for a specific time, and when that time is reached, a sound will be played as a notification.

## Features

- **Graphical User Interface**: Easy-to-use interface built with Tkinter.
- **Custom Alarm Time**: Set the alarm for any time of day.
- **Sound Notification**: Plays a sound file when the alarm time is reached.

## Requirements

- Python 3.x
- Tkinter library (usually included with Python)
- `datetime` and `time` modules (included with Python)
- `winsound` module (Windows-specific for playing sound)
- Sound file named `sound.wav` in the same directory as the program

## Installation

1. Ensure Python 3.x is installed on your system.
2. Place the program file and the `sound.wav` file in the same directory.

## Usage

1. **Start the Program**: Run the program. A window titled "Alarm Clock" will open.
   
2. **Set Alarm Time**:
   - Use the drop-down menus to select the hour, minute, and second for the alarm.
   - The time format is 24-hour.

3. **Activate the Alarm**:
   - Click the "Set Alarm" button to activate the alarm.
   - The program will continuously check the current time and compare it with the set alarm time.

4. **Alarm Trigger**:
   - When the current time matches the set alarm time, the program will print "Time to Wake up" in the console and play the `sound.wav` file.

5. **Closing the Program**: 
   - Close the window or terminate the program to stop the alarm.

## Notes

- The program must remain running for the alarm to work.
- Make sure the sound file `sound.wav` is in the correct format and not corrupted.
- This program is designed for Windows systems (due to `winsound`). Modifications are needed for other operating systems.

## Troubleshooting

- **No Sound Playing**: Ensure `sound.wav` is in the same directory as the program and that your audio device is functioning correctly.
- **Tkinter not found**: Install Tkinter using your Python package manager (e.g., `pip install tk`).
- **Program not running**: Make sure Python 3.x is properly installed and that you are running the program with Python 3.x.