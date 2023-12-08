'''
This is the main file of the Image to PDF Converter software. It contains the GUI implementation and handles the user interactions.
'''
import tkinter as tk
from tkinter import filedialog
import os
import img2pdf
class ImageToPDFConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.label = tk.Label(root, text="Select the directory containing the JPG images:")
        self.label.pack(pady=10)
        self.button = tk.Button(root, text="Browse", command=self.select_directory)
        self.button.pack(pady=5)
        self.convert_button = tk.Button(root, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack(pady=5)
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)
    def select_directory(self):
        self.directory = filedialog.askdirectory()
        self.status_label.config(text="Selected directory: " + self.directory)
    def convert_to_pdf(self):
        if hasattr(self, 'directory'):
            images = [f for f in os.listdir(self.directory) if f.endswith('.jpg')]
            if images:
                output_pdf = os.path.join(self.directory, 'output.pdf')
                with open(output_pdf, "wb") as f:
                    f.write(img2pdf.convert([os.path.join(self.directory, image) for image in images]))
                self.status_label.config(text="Conversion successful. PDF saved as output.pdf")
            else:
                self.status_label.config(text="No JPG images found in the directory.")
        else:
            self.status_label.config(text="Please select a directory first.")
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToPDFConverterApp(root)
    root.mainloop()