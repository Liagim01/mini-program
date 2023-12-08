'''
This class will handle the conversion of PDFs into text files.
'''
class PDFExporter:
    def __init__(self, pdf_parser):
        self.pdf_parser = pdf_parser
    def export_to_text(self):
        pdf_content = self.pdf_parser.extracted_content
        self.pdf_parser.file_manager.write_file(pdf_content)