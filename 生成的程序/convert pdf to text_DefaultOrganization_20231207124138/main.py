import io
import PyPDF2
import os
from filemanager import FileManager
from pdfparser import PDFParser
from pdfexporter import PDFExporter
# Prompt the user to enter the PDF file path
pdf_file_path = input("Enter the path to the PDF file: ")
# Instantiate the FileManager
file_manager = FileManager(pdf_file_path)
# Instantiate the PDFParser
pdf_parser = PDFParser(file_manager)
# Extract the content from the PDF file
pdf_content = pdf_parser.extract_content()
# Instantiate the PDFExporter
pdf_exporter = PDFExporter(pdf_parser)
# Export the PDF content to a text file
pdf_exporter.export_to_text()
# Print a success message
print("PDF to text conversion completed successfully.")