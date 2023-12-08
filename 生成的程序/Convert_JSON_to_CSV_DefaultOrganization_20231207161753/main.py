'''
This script converts a JSON file to a CSV file format.
Instructions:
1. Install the Python 3.x environment. This can be done through the official website, available through the Python Software Foundation.
2. Create a valid JSON file containing comma-separated values (CSV) and save it as 'input.json'.
3. Place the JSON file in the same directory as the script.
4. Run the script 'converter.py' within the Python 3.x environment.
5. The script will generate an 'output.csv' file in the same directory as the script.
Note: No additional modules are required for the program outside of the standard Python library. It is important to ensure that the 'input.json' is valid prior to running the script. Any errors will be recorded within the program during use.
'''
import json
import csv
import os
def convert_json_to_csv(json_file):
    if not os.path.exists(json_file):
        print("File not found!")
        return
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list) or len(data) == 0 or not isinstance(data[0], dict):
                print("Invalid JSON file format!")
                return
            csv_file = json_file.replace(".json", ".csv")
            with open(csv_file, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data[0].keys())
                for item in data:
                    writer.writerow(item.values())
            print("Conversion successful!")
    except FileNotFoundError:
        print("File not found!")
    except json.JSONDecodeError:
        print("Invalid JSON file!")
if __name__ == "__main__":
    json_file = "input.json"
    convert_json_to_csv(json_file)