'''
This is the main file that initializes the GUI and handles user interactions.
'''
import tkinter as tk
from tkinter import messagebox
from frame_capture import FrameCapture
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Video Frame Capture")
        self.geometry("400x200")
        self.file_path_entry = tk.Entry(self)
        self.file_path_entry.pack()
        self.directory_entry = tk.Entry(self)
        self.directory_entry.pack()
        self.capture_button = tk.Button(self, text="Capture Frames", command=self.capture_frames)
        self.capture_button.pack()
    def capture_frames(self):
        file_path = self.file_path_entry.get()
        directory = self.directory_entry.get()
        frame_capture = FrameCapture(file_path)
        try:
            frame_capture.capture_frames(directory)
            messagebox.showinfo("Frames Captured", "Frames captured successfully!")
        except cv2.error as e:
            messagebox.showerror("Error", f"Error capturing frames: {str(e)}")
if __name__ == "__main__":
    app = Application()
    app.mainloop()