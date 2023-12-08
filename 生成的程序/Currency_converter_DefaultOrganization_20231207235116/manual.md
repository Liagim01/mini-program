# Currency Converter User Manual

## Introduction

The Currency Converter program is a Python-based application that allows users to quickly and easily convert currency values from one currency to another with live exchange rate information. It also provides a list of available currencies and allows users to quit the program at any time.

## Prerequisites

Before using the Currency Converter program, please ensure that the following prerequisites are met:

1. Python 3 must be installed on your system.
2. The Requests library must be installed. You can install it by running the following command in your terminal:

   ```
   pip install requests
   ```

## Installation

To install and run the Currency Converter program, please follow these steps:

1. Download the `cc.py` file from the GitHub repository created by `github-of-wone`.

2. Open the terminal and navigate to the directory where the `cc.py` file is located.

3. Run the following command to execute the script:

   ```
   python cc.py
   ```

## Usage

Once the Currency Converter program is running, you can follow the on-screen instructions to specify the amount to convert, the source currency, and the target currency.

- Enter the amount to convert when prompted.
- Enter the source currency code (e.g., USD, EUR) when prompted.
- Enter the target currency code (e.g., USD, EUR) when prompted.

The program will fetch live exchange rate information using the Fixer.io API and display the converted amount.

You can also use the following commands:

- `SHOW`: Type `SHOW` to see a list of available currencies.
- `Q`: Type `Q` to quit the program.

## Example

Here is an example of how to use the Currency Converter program:

```
Amount: 100
Source Currency: USD
Target Currency: EUR

Output: 100 USD = 85.23 EUR
```

## Support

If you encounter any issues or have any questions regarding the Currency Converter program, please reach out to our support team at support@chatdev.com.