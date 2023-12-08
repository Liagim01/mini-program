'''
This file contains the GUI class for the software.
'''
import tkinter as tk
from tkinter import messagebox
class GUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Create GUI elements
        self.button = tk.Button(self, text="Click Me", command=self.handle_button_click)
        self.button.pack()
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Option 1", command=self.handle_menu_selection)
        self.menu.add_command(label="Option 2", command=self.handle_menu_selection)
        self.master.config(menu=self.menu)
        # Set up layout
        self.pack()
    def handle_button_click(self):
        # Handle button click event
        messagebox.showinfo("Button Clicked", "Button was clicked!")
    def handle_menu_selection(self):
        # Handle menu selection event
        messagebox.showinfo("Menu Selected", "Menu item was selected!")