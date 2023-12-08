'''
This program is designed to convert images in JPEG format to the PNG format.
Requirements:
1. A system with Python 3.x installed
2. Pillow module installed with pip
To use the terminal-based script:
1. Place a JPEG image named ‘input.jpeg’ in the same directory as the script.
2. Run the terminal script (e.g., ‘converter_terminal.py’): `python converter_terminal.py`
3. The converted PNG image will be saved in the same directory.
To use the GUI-based script:
1. Run the GUI script (e,g., ‘converter_GUI.py’): `python converter_GUI.py`
2. Select a JPEG image and choose the desired location to save the converted PNG file.
3. Error handling for the case of an image not being selected.
'''
from tkinter import messagebox
from tkinter import Tk, filedialog
from PIL import Image
def select_image():
    root = Tk()
    root.withdraw()
    image_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpeg")])
    return image_path
def select_save_location():
    root = Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    return save_path
def convert_image():
    input_image_path = select_image()
    if input_image_path:
        output_image_path = select_save_location()
        if output_image_path:
            image = Image.open(input_image_path)
            image.save(output_image_path)
            messagebox.showinfo("Conversion Successful", "Image saved as output.png")
        else:
            messagebox.showerror("Error", "No save location selected.")
    else:
        messagebox.showerror("Error", "No image selected.")
if __name__ == "__main__":
    convert_image()