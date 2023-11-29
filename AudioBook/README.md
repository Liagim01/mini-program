# AudioBook Generator

## Description
This Python application converts text from a PDF file into an MP3 audio file, effectively creating an audiobook. It uses the Google Text to Speech (gTTS) library for text-to-speech conversion and PyPDF2 for reading PDF files.

## Installation

Before running the script, you need to install the required libraries. Open your terminal or command prompt and execute the following commands:

```bash
pip install gtts
pip install PyPDF2
```

These commands will install the Google Text to Speech (gTTS) library and PyPDF2 library needed for the application to function.

## Usage

1. **Prepare Your PDF File**:
   - Ensure the PDF file you want to convert is in the same directory as the script or provide the full path to the file.
   - Replace `'name.pdf'` in the script with the name of your PDF file.

2. **Run the Application**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script by executing:

     ```bash
     python Audio-book.py
     ```

3. **Output**:
   - The script will read the text from the PDF file and convert it into an MP3 file.
   - The generated MP3 file, named `Audio.mp3`, will be saved in the same directory as the script.

## Features

- **PDF to Speech**: Converts text from any readable PDF file into spoken words.
- **Customizable Speech**:
  - Set the language by changing the `language` variable. Default is English (`'en'`).
  - Control the speed of speech by setting `slow` to `True` or `False`.
- **Batch Processing**: Capable of processing multiple pages from a PDF file.

## Note

- The effectiveness of text extraction may vary depending on the PDF's format and layout.
- This script currently supports English language. For other languages, modify the `language` variable accordingly.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository, make changes, and submit pull requests.

*This is an open-source project and is available for free use and modification under the MIT License.*