'''
This is the main file of the Battery Notificator program.
It checks the battery percentage and triggers a desktop notification if the battery is low.
'''
import psutil
from py_notificator import Notificator
def check_battery():
    if hasattr(psutil, 'sensors_battery'):
        battery = psutil.sensors_battery()
        print(battery)
    #     plugged = battery.power_plugged
    #     percent = battery.percent
    #     if percent <= 30 and not plugged:
    #         message = f"The battery is at {percent}% and is low."
    #         notifier = Notificator()
    #         notifier.notify(message)
    # else:
    #     print("Battery information is not available on this platform.")
if __name__ == "__main__":
    check_battery()