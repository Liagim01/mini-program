'''
This file contains the Audiobook class responsible for generating the audio book.
'''
import os
from gtts import gTTS
import PyPDF2
class Audiobook:
    def __init__(self, file_path):
        self.file_path = file_path
    def generate_audio_book(self):
        pdf_file = None  # Define pdf_file variable and set it to None
        try:
            pdf_file = open(self.file_path, 'rb')
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            audio_text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                audio_text += page.extract_text()
            language = 'en'
            slow = False
            audio = gTTS(text=audio_text, lang=language, slow=slow)
            audio.save("Audio.mp3")
        except Exception as e:
            print("An error occurred while generating the audio book:", str(e))
        finally:
            if pdf_file is not None:  # Check if pdf_file is not None before closing
                pdf_file.close()