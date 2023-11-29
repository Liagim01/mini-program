# JSON to CSV Converter

## Overview

This Python script is designed to convert a JSON file into a CSV format. It reads a JSON file, extracts data, and formats it into a CSV file, making it useful for data transformation and integration tasks.

## Purpose

The script's primary purpose is to facilitate the conversion of data from JSON format, commonly used in web applications and APIs, to CSV format, which is widely used in data analysis, spreadsheets, and database applications.

## Prerequisites

- Python 3.x
- No additional modules are required beyond the standard Python library.

### Note on Installation
The JSON module is part of Python's standard library, so there's no need to install it separately. The instruction `pip install json` is unnecessary and can be ignored.

## How to Run the Script

1. Ensure Python 3.x is installed on your system.
2. Place the JSON file you want to convert in the same directory as the script. Name this file `input.json`.
3. Run the script:

   ```bash
   python converter.py
   ```

4. The script will create an `output.csv` file in the same directory.

## Script Details

### Functionality

- Reads data from a file named `input.json`.
- Parses the JSON data and converts it into a CSV format.
- Saves the converted data to a file named `output.csv`.
- Handles exceptions and displays error messages if any issues arise during the conversion process.

### Usage Example

Before running the script, ensure that `input.json` contains valid JSON data. For instance:

```json
[
    {"Name": "John Doe", "age": 30, "birthyear": 1991},
    {"Name": "Jane Smith", "age": 25, "birthyear": 1996}
]
```

After running the script, `output.csv` will contain:

```
Name,age,birthyear
John Doe,30,1991
Jane Smith,25,1996
```
