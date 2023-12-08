import tkinter as tk
from website_status_checker import WebsiteStatusChecker
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Website Status Checker")
        self.geometry("400x300")
        self.label = tk.Label(self, text="Enter the path to the websites.txt file:")
        self.label.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button = tk.Button(self, text="Check Status", command=self.check_status)
        self.button.pack()
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
    def check_status(self):
        file_path = self.entry.get()
        checker = WebsiteStatusChecker(file_path)
        result = checker.check_status()
        self.result_label.config(text=result)
if __name__ == "__main__":
    app = Application()
    app.mainloop()