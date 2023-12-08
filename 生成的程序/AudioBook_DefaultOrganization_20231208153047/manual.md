# Audiobook Generator User Manual

## Introduction

The Audiobook Generator is a Python application that allows you to convert PDF files into audio books. It uses the Google Text to Speech library (gtts) and the PyPDF2 library to read the text from a PDF file and convert it into an MP3 file.

## Installation

To use the Audiobook Generator, you need to have Python 3 installed on your computer. You also need to install the required dependencies, which are the gtts library and the PyPDF2 library.

1. Open a terminal window on your computer.
2. Execute the following commands to install the dependencies:

```bash
pip install gtts
pip install PyPDF2
```

## Usage

To convert a PDF file into an audio book using the Audiobook Generator, follow these steps:

1. Place the PDF file you wish to convert into an audio book in the same directory as the `Audio-book.py` file. Alternatively, provide the full path to the file.
2. Open a terminal window and navigate to the directory containing the `Audio-book.py` file.
3. Run the `Audio-book.py` file by executing the following command:

```bash
python Audio-book.py
```

4. The script will read the text from the PDF file and convert it into an MP3 file. The resulting MP3 file, named `Audio.mp3`, will be saved in the same directory.

## Customization

If needed, you can modify the language variable to support languages other than English. The default language is set to 'en'.

To control the speed of speech, you can set the slow variable to True or False. The default value is False, which means the speech will be generated at a normal speed.

## Batch Processing

The Audiobook Generator is capable of processing multiple pages from a PDF file. It will read the text from each page and concatenate them into a single audio file.

## Note

Please note that depending on the layout and formatting of the PDF file, the text extraction may be less effective.