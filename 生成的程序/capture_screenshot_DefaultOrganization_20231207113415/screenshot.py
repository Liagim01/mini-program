'''
This file contains the capture_screenshot function which captures a screenshot and saves it to the specified path.
'''
import pyautogui
def capture_screenshot(path):
    # Capture a screenshot using pyautogui and save it to the specified path
    screenshot = pyautogui.screenshot()
    screenshot.save(path)