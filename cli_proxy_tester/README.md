

# CLI-Based Proxy Tester

## Overview

This Python script is a command-line interface (CLI) based proxy tester. It allows users to test individual proxies, (re)test a list of proxies from a CSV file, and add and test proxies from a text file. The script uses the `requests` library for HTTP requests, `pandas` for handling CSV files, and `click` for creating the CLI.

## Purpose

The script's primary purpose is to automate the process of testing proxies for their functionality. It's useful for users who need to verify the operational status of their proxies.

## Prerequisites

- Python 3.x
- `requests` and `pandas` libraries installed, which can be done via pip:

  ```bash
  pip install requests pandas
  ```

## How to Run the Script

1. Ensure Python 3.x and the required libraries are installed.
2. Download the script to your local machine.
3. Run the script from the command line using the provided CLI commands.

## Script Details

### Main Functions

- `test_single_proxy(proxy, iptest, csv)`: Tests an individual proxy and adds it to a CSV file.
- `test_csv_file(iptest, csv)`: (Re)tests every proxy in a given CSV file.
- `add_from_text_file(iptest, txt, csv)`: Adds a list of proxies from a text file and tests them.

### CLI Commands

- Test a single proxy: `python cli.py single http://1.1.1.1`
- Test a single proxy with a custom iptest address: `python cli.py single http://1.1.1.1 --iptest iptest.yourdomain.com`
- (Re)test all proxies in a CSV file: `python cli.py csv-file proxies.csv`
- Add and test proxies from a text file: `python cli.py add-from-txt-file proxy_candidates.txt`

### Usage Examples

1. To test a single HTTP proxy `1.1.1.1`: 
   ```bash
   python cli.py single http://1.1.1.1
   ```
2. To (re)test all proxies listed in `proxies.csv`:
   ```bash
   python cli.py csv-file proxies.csv
   ```
3. To add and test each proxy listed in `proxy_candidates.txt`:
   ```bash
   python cli.py add-from-txt-file proxy_candidates.txt
   ```

## Author

Ingo Kleiber (ingo@kleiber.me)

