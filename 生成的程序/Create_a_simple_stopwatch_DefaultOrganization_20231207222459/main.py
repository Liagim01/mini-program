'''
This is the main file that creates a simple stopwatch using Python, the Tkinter library, and the datetime library.
'''
import tkinter as tk
from datetime import datetime, timedelta
class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.is_running = False
        self.start_time = None
        self.elapsed_time = timedelta()
        self.time_label = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.time_label.pack(pady=20)
        self.start_button = tk.Button(root, text="Start", command=self.start_stopwatch)
        self.start_button.pack(pady=10)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_stopwatch, state=tk.DISABLED)
        self.reset_button.pack(pady=10)
    def start_stopwatch(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
    def stop_stopwatch(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time += datetime.now() - self.start_time
            self.start_time = None  # Reset the start time
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = None
        self.elapsed_time = timedelta()
        self.time_label.config(text="00:00:00")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)
    def update_time(self):
        if self.is_running:
            elapsed = self.elapsed_time + (datetime.now() - self.start_time)
            hours, remainder = divmod(elapsed.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
            self.time_label.config(text=time_string)
            self.root.after(1000, self.update_time)
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()