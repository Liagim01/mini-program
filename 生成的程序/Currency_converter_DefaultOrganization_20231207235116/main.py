'''
Currency Converter Program
'''
import tkinter as tk
import requests
import os
class CurrencyConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Currency Converter")
        self.amount_label = tk.Label(self.window, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.window)
        self.amount_entry.pack()
        self.source_currency_label = tk.Label(self.window, text="Source Currency:")
        self.source_currency_label.pack()
        self.source_currency_entry = tk.Entry(self.window)
        self.source_currency_entry.pack()
        self.target_currency_label = tk.Label(self.window, text="Target Currency:")
        self.target_currency_label.pack()
        self.target_currency_entry = tk.Entry(self.window)
        self.target_currency_entry.pack()
        self.convert_button = tk.Button(self.window, text="Convert", command=self.convert_currency)
        self.convert_button.pack()
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()
        self.show_button = tk.Button(self.window, text="Show Currencies", command=self.show_currencies)
        self.show_button.pack()
        self.quit_button = tk.Button(self.window, text="Quit", command=self.window.quit)
        self.quit_button.pack()
    def run(self):
        self.window.mainloop()
    def convert_currency(self):
        amount = self.amount_entry.get()
        source_currency = self.source_currency_entry.get()
        target_currency = self.target_currency_entry.get()
        api_key = os.getenv("FIXER_API_KEY")  # Retrieve API key from environment variable
        if amount and source_currency and target_currency:
            try:
                amount = float(amount)
                response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{source_currency}")
                data = response.json()
                rates = data.get("rates")
                if rates and target_currency in rates:
                    rate = rates[target_currency]
                    converted_amount = amount * rate
                    self.result_label.config(text=f"{amount} {source_currency} = {converted_amount} {target_currency}")
                else:
                    self.result_label.config(text="Invalid source or target currency")
            except ValueError:
                self.result_label.config(text="Invalid amount")
            except requests.exceptions.RequestException:
                self.result_label.config(text="Failed to fetch exchange rate")
        else:
            self.result_label.config(text="Please enter all fields")
    def show_currencies(self):
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        currencies = list(data["rates"].keys())
        self.result_label.config(text=", ".join(currencies))
if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()