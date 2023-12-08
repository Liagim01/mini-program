'''
This file contains the Calculator class which represents the calculator application.
'''
import tkinter as tk
from tkinter import messagebox
import ast
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.input_field = tk.Entry(self.root, width=20)
        self.input_field.grid(row=0, column=0, columnspan=4)
        self.buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("^", 4, 2), ("+", 4, 3)
        ]
        self.create_buttons()
        self.clear_button = tk.Button(self.root, text="C", width=5, command=self.clear_input)
        self.clear_button.grid(row=5, column=0)
        self.backspace_button = tk.Button(self.root, text="<-", width=5, command=self.remove_last_character)
        self.backspace_button.grid(row=5, column=1)
        self.quit_button = tk.Button(self.root, text="Quit", width=5, command=self.root.quit)
        self.quit_button.grid(row=5, column=2)
        self.equal_button = tk.Button(self.root, text="=", width=5, command=self.calculate)
        self.equal_button.grid(row=5, column=3)
    def create_buttons(self):
        for button_text, row, column in self.buttons:
            button = tk.Button(self.root, text=button_text, width=5, command=lambda text=button_text: self.append_input(text))
            button.grid(row=row, column=column)
    def append_input(self, text):
        self.input_field.insert(tk.END, text)
    def clear_input(self):
        self.input_field.delete(0, tk.END)
    def remove_last_character(self):
        current_input = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.input_field.insert(tk.END, current_input[:-1])
    def calculate(self):
        try:
            expression = self.input_field.get()
            result = ast.literal_eval(expression)
            self.input_field.delete(0, tk.END)
            self.input_field.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
        except Exception as e:
            messagebox.showerror("Error", str(e))