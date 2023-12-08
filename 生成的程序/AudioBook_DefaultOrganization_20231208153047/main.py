'''
This is the main file that serves as the entry point for the Audiobook Generator application.
'''
import tkinter as tk
from tkinter import filedialog
from audiobook import Audiobook
def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        audiobook = Audiobook(file_path)
        audiobook.generate_audio_book()
root = tk.Tk()
root.title("Audiobook Generator")
select_pdf_button = tk.Button(root, text="Select PDF File", command=select_pdf_file)
select_pdf_button.pack()
root.mainloop()