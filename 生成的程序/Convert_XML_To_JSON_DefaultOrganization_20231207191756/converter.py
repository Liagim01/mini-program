'''
This file contains the implementation of the ConverterApp class for XML to JSON conversion.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
import xmltodict
import json
class ConverterApp(tk.Tk):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title("XML to JSON Converter")
        self.geometry("400x200")
        self.btn_convert = tk.Button(self, text="Convert", command=self.convert)
        self.btn_convert.pack(pady=10)
    def convert(self):
        # Open file dialog to select XML file
        file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
        if file_path:
            try:
                # Read XML content
                with open(file_path, "r") as xml_file:
                    xml_content = xml_file.read()
                # Convert XML to Python dictionary
                xml_dict = xmltodict.parse(xml_content)
                # Convert dictionary to JSON string
                json_str = json.dumps(xml_dict, indent=4)
                # Save JSON string to output.json
                with open("output.json", "w") as json_file:
                    json_file.write(json_str)
                messagebox.showinfo("Conversion Successful", "XML to JSON conversion completed.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("No File Selected", "Please select an XML file.")