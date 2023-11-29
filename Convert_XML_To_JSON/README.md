
# Converter

This Python script provides a straightforward and efficient way to convert XML files to JSON format. It's particularly useful for projects requiring data transformation or for integrating XML data into systems that predominantly use JSON.

### Prerequisites
- Python 3
- `xmltodict` library, which can be installed using pip:
  ```
  $ pip install xmltodict
  ```

### Description
The script converts an XML file named `input.xml` into a JSON file named `output.json`. It leverages the `xmltodict` library to parse the XML data and then uses Python's `json` module to format and output the data as JSON.

### Detailed Explanation of the Code
1. **Import Libraries**: The script begins by importing necessary libraries - `json` for JSON processing and `xmltodict` for converting XML to a Python dictionary.
2. **Reading XML File**: It opens and reads the content of `input.xml`.
3. **XML to Dictionary Conversion**: Using `xmltodict.parse`, the XML data is converted into a Python dictionary.
4. **Dictionary to JSON Conversion**: This dictionary is then converted to a JSON string using `json.dumps`.
5. **Writing JSON to File**: Finally, the JSON string is written to `output.json`, thus completing the conversion process.

### How to Run the Script
1. Rename your XML file to `input.xml`.
2. Execute the script using the command:
   ```
   python3 converter.py
   ```
3. The converted JSON data will be saved in a file named `output.json`.

### Functionality Added
- **File Management**: The script now includes proper file handling using `with` statements. This ensures that files are correctly opened and closed after their operation is completed, enhancing the robustness of the script.
- **Exception Handling**: [Add details if exception handling or other functionalities are added.]

### Author
Azhad Ghufran

