'''
This class will parse PDF files and process them for use in the program.
'''
import PyPDF2
class PDFParser:
    def __init__(self, file_manager):
        self.file_manager = file_manager
        self.extracted_content = ""
    def extract_content(self):
        pdf_reader = PyPDF2.PdfFileReader(self.file_manager.read_file())
        num_pages = pdf_reader.numPages
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            self.extracted_content += page.extractText()
        return self.extracted_content