'''
This is the main program file that serves as the entry point for the software.
'''
import tkinter as tk
from tkinter import messagebox
# Import other necessary modules and classes
from gui import GUI
from data import Data
from error_handling import ErrorHandler
from utils import Utility
# Define the main application class
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Software")
        self.geometry("400x300")
        # Initialize variables
        # Set up data structures
        self.data = Data()
        # Create GUI elements
        self.gui = GUI(self)
        # Set up event handlers
        self.error_handler = ErrorHandler()
        # Start the main event loop
        self.mainloop()
# Create an instance of the Application class
if __name__ == "__main__":
    app = Application()