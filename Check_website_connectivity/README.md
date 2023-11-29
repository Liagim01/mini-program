
# Website Status Checker

## Overview

This Python script checks the status of websites listed in a text file and records their operational status in a CSV file. It utilizes the `requests` library to make HTTP requests and determine if each website is working based on the HTTP status code returned.

## Purpose

The script's primary purpose is to automate the process of checking the availability of multiple websites, which can be useful for monitoring website uptime or validating a list of URLs.

## Prerequisites

- Python 3.x installed on your system.
- `requests` library installed, which can be done via pip:

  ```bash
  pip install requests
  ```

## How to Run the Script

1. Ensure Python 3.x and the `requests` library are installed.
2. Create a text file named `websites.txt` and list the URLs of websites you want to check, each on a new line.
3. Run the script using the following command:

   ```bash
   python check_website_status.py
   ```

## Script Details

### Functionality

- Reads a list of websites from `websites.txt`.
- Checks each website's status by sending an HTTP GET request.
- Records whether each website is 'working' or 'not working' based on the HTTP status code 200.
- Outputs the results to `website_status.csv`.

### Output Format

The script generates a CSV file named `website_status.csv` with two columns: 
- `Website`: The URL of the website.
- `Status`: Indicates 'working' if the website is operational (HTTP status 200) or 'not working' otherwise.

### Example Usage

Create a `websites.txt` file with the following content:

```
https://www.example.com
https://www.nonexistentwebsite.com
```

Run the script, and then check `website_status.csv` for the output.

