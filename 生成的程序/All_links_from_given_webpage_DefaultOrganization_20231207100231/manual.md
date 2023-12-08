# Hyperlink Extractor User Manual

## Introduction

The Hyperlink Extractor is a Python script that allows you to extract all hyperlinks from a specified webpage and save them to a text file. This user manual will guide you through the installation process and explain how to use the script effectively.

## Installation

To install the Hyperlink Extractor, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the script files from the provided source.

3. Open your terminal or command prompt and navigate to the directory where the script files are located.

4. Install the required modules by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the BeautifulSoup4 and requests modules.

## Usage

To use the Hyperlink Extractor, follow these steps:

1. Open your terminal or command prompt and navigate to the directory where the script (`get_links.py`) is located.

2. Execute the script by running the following command:

   ```
   python get_links.py
   ```

3. When prompted, enter the URL of the webpage you want to analyze.

4. The script will process the webpage and store all extracted links as an array in a file named `myLinks.txt` in the same directory.

5. After successful execution, you'll find a file named `myLinks.txt` in the script's directory. This file contains all the hyperlinks extracted from the specified webpage stored as an array.

## Example

Let's walk through an example to demonstrate how to use the Hyperlink Extractor.

1. Open your terminal or command prompt and navigate to the directory where the script (`get_links.py`) is located.

2. Execute the script by running the following command:

   ```
   python get_links.py
   ```

3. When prompted, enter the URL of the webpage you want to analyze. For example, enter `https://www.example.com`.

4. The script will process the webpage and store all extracted links as an array in a file named `myLinks.txt` in the same directory.

5. After successful execution, you'll find a file named `myLinks.txt` in the script's directory. Open the file to view the extracted hyperlinks.

## Troubleshooting

If you encounter any issues while using the Hyperlink Extractor, please check the following:

- Make sure you have installed the required modules (`BeautifulSoup4` and `requests`) correctly.

- Ensure that you have a stable internet connection to access the specified webpage.

- Double-check the URL you entered to analyze the correct webpage.

If the issue persists, please contact our support team for further assistance.

## Conclusion

The Hyperlink Extractor is a powerful tool for extracting hyperlinks from webpages. By following the instructions in this user manual, you can easily install and use the script to extract hyperlinks and save them to a text file. Enjoy using the Hyperlink Extractor and feel free to reach out to our support team if you have any questions or feedback.