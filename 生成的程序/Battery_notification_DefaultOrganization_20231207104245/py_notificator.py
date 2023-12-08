'''
This file contains the Notificator class, which is responsible for sending desktop notifications.
'''
import platform
class Notificator:
    def __init__(self):
        self.os = platform.system()
    def notify(self, message):
        if self.os == "Windows":
            self._notify_windows(message)
        else:
            self._notify_generic(message)
    def _notify_windows(self, message):
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast("Battery Notificator", message, duration=10)
        except ImportError:
            print("win10toast package is not installed. Please install it using 'pip install win10toast'.")
    def _notify_generic(self, message):
        # Implement notification logic for other operating systems
        # For now, we will print the message as a placeholder
        print(f"Notification: {message}")