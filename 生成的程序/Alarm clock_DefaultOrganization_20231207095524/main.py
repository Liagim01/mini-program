'''
Alarm Clock Program
'''
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, time
import winsound
class AlarmClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.hour_var = tk.StringVar()
        self.minute_var = tk.StringVar()
        self.second_var = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        hour_label = tk.Label(self.root, text="Hour:")
        hour_label.grid(row=0, column=0, padx=10, pady=10)
        hour_dropdown = tk.OptionMenu(self.root, self.hour_var, *range(24))
        hour_dropdown.grid(row=0, column=1, padx=10, pady=10)
        minute_label = tk.Label(self.root, text="Minute:")
        minute_label.grid(row=1, column=0, padx=10, pady=10)
        minute_dropdown = tk.OptionMenu(self.root, self.minute_var, *range(60))
        minute_dropdown.grid(row=1, column=1, padx=10, pady=10)
        second_label = tk.Label(self.root, text="Second:")
        second_label.grid(row=2, column=0, padx=10, pady=10)
        second_dropdown = tk.OptionMenu(self.root, self.second_var, *range(60))
        second_dropdown.grid(row=2, column=1, padx=10, pady=10)
        set_button = tk.Button(self.root, text="Set Alarm", command=self.set_alarm)
        set_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    def set_alarm(self):
        try:
            hour = int(self.hour_var.get())
            minute = int(self.minute_var.get())
            second = int(self.second_var.get())
            now = datetime.now().time()
            alarm_time = time(hour, minute, second)
            if now >= alarm_time:
                messagebox.showerror("Invalid Time", "Please select a future time.")
                return
            self.check_alarm(alarm_time)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please select valid hour, minute, and second.")
    def check_alarm(self, alarm_time):
        now = datetime.now().time()
        if now >= alarm_time:
            messagebox.showinfo("Alarm", "Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        else:
            self.root.after(1000, self.check_alarm, alarm_time)
if __name__ == "__main__":
    root = tk.Tk()
    alarm_clock = AlarmClock(root)
    root.mainloop()