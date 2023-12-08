'''
Billing System
This script implements a comprehensive billing system using Python and Tkinter GUI package.
It simplifies the billing process in various types of stores.
Author: [Your Name]
'''
import tkinter as tk
from tkinter import simpledialog, messagebox
import os
class BillingSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Billing System")
        # Initialize variables
        self.product_details = []
        self.customer_info = {}
        self.total_price = 0.0
        self.total_taxes = 0.0
        # Create GUI elements
        self.create_product_frame()
        self.create_customer_frame()
        self.create_button_frame()
        # Start the main loop
        self.root.mainloop()
    def create_product_frame(self):
        # Create product frame
        self.product_frame = tk.LabelFrame(self.root, text="Product Details")
        self.product_frame.pack(padx=10, pady=10)
        # Create product name label and entry
        self.product_name_label = tk.Label(self.product_frame, text="Product Name:")
        self.product_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.product_name_entry = tk.Entry(self.product_frame)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)
        # Create product price label and entry
        self.product_price_label = tk.Label(self.product_frame, text="Product Price:")
        self.product_price_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.product_price_entry = tk.Entry(self.product_frame)
        self.product_price_entry.grid(row=1, column=1, padx=5, pady=5)
        # Create product quantity label and entry
        self.product_quantity_label = tk.Label(self.product_frame, text="Product Quantity:")
        self.product_quantity_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.product_quantity_entry = tk.Entry(self.product_frame)
        self.product_quantity_entry.grid(row=2, column=1, padx=5, pady=5)
        # Create add product button
        self.add_product_button = tk.Button(self.product_frame, text="Add Product", command=self.add_product)
        self.add_product_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    def create_customer_frame(self):
        # Create customer frame
        self.customer_frame = tk.LabelFrame(self.root, text="Customer Information")
        self.customer_frame.pack(padx=10, pady=10)
        # Create customer name label and entry
        self.customer_name_label = tk.Label(self.customer_frame, text="Customer Name:")
        self.customer_name_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.customer_name_entry = tk.Entry(self.customer_frame)
        self.customer_name_entry.grid(row=0, column=1, padx=5, pady=5)
        # Create customer email label and entry
        self.customer_email_label = tk.Label(self.customer_frame, text="Customer Email:")
        self.customer_email_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.customer_email_entry = tk.Entry(self.customer_frame)
        self.customer_email_entry.grid(row=1, column=1, padx=5, pady=5)
        # Create customer phone label and entry
        self.customer_phone_label = tk.Label(self.customer_frame, text="Customer Phone:")
        self.customer_phone_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.customer_phone_entry = tk.Entry(self.customer_frame)
        self.customer_phone_entry.grid(row=2, column=1, padx=5, pady=5)
        # Create generate bill button
        self.generate_bill_button = tk.Button(self.customer_frame, text="Generate Bill", command=self.generate_bill)
        self.generate_bill_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    def create_button_frame(self):
        # Create button frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(padx=10, pady=10)
        # Create search bill button
        self.search_bill_button = tk.Button(self.button_frame, text="Search Bill", command=self.search_bill)
        self.search_bill_button.grid(row=0, column=0, padx=5, pady=5)
        # Create exit button
        self.exit_button = tk.Button(self.button_frame, text="Exit", command=self.root.quit)
        self.exit_button.grid(row=0, column=1, padx=5, pady=5)
    def add_product(self):
        # Get product details from the entries
        product_name = self.product_name_entry.get()
        product_price = float(self.product_price_entry.get())
        product_quantity = int(self.product_quantity_entry.get())
        # Calculate total price and taxes
        total_product_price = product_price * product_quantity
        total_product_taxes = total_product_price * 0.1
        # Add product details to the list
        self.product_details.append(
            (product_name, product_price, product_quantity, total_product_price, total_product_taxes))
        # Clear the entries
        self.product_name_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        self.product_quantity_entry.delete(0, tk.END)
        # Show success message
        messagebox.showinfo("Success", "Product added successfully!")
    def generate_bill(self):
        # Get customer information from the entries
        customer_name = self.customer_name_entry.get()
        customer_email = self.customer_email_entry.get()
        customer_phone = self.customer_phone_entry.get()
        # Check if any product is added
        if len(self.product_details) == 0:
            messagebox.showerror("Error", "No product added!")
            return
        # Calculate total price and taxes
        for product in self.product_details:
            self.total_price += product[3]
            self.total_taxes += product[4]
        # Create bill text
        bill_text = f"Customer Name: {customer_name}\n"
        bill_text += f"Customer Email: {customer_email}\n"
        bill_text += f"Customer Phone: {customer_phone}\n\n"
        bill_text += "Product Details:\n"
        bill_text += "-----------------\n"
        for product in self.product_details:
            bill_text += f"Product Name: {product[0]}\n"
            bill_text += f"Product Price: {product[1]}\n"
            bill_text += f"Product Quantity: {product[2]}\n"
            bill_text += f"Total Price: {product[3]}\n"
            bill_text += f"Total Taxes: {product[4]}\n"
            bill_text += "-----------------\n"
        bill_text += f"Total Price: {self.total_price}\n"
        bill_text += f"Total Taxes: {self.total_taxes}\n"
        # Save bill as a text file
        bill_file = open("bill.txt", "w")
        bill_file.write(bill_text)
        bill_file.close()
        # Clear the entries and product details
        self.customer_name_entry.delete(0, tk.END)
        self.customer_email_entry.delete(0, tk.END)
        self.customer_phone_entry.delete(0, tk.END)
        self.product_details = []
        self.total_price = 0.0
        self.total_taxes = 0.0
        # Show success message
        messagebox.showinfo("Success", "Bill generated successfully!")
    def search_bill(self):
        # Get bill number from the user
        bill_number = simpledialog.askstring("Search Bill", "Enter Bill Number:")
        # Check if bill number is provided
        if bill_number is None:
            return
        # Check if bill file exists
        if not os.path.exists(f"bill_{bill_number}.txt"):
            messagebox.showerror("Error", "Bill not found!")
            return
        # Open and display the bill file
        bill_file = open(f"bill_{bill_number}.txt", "r")
        bill_text = bill_file.read()
        bill_file.close()
        messagebox.showinfo("Bill Details", bill_text)
# Run the Billing System
if __name__ == "__main__":
    billing_system = BillingSystem()