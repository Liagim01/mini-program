'''
This class is responsible for handling file operations, including reading and writing.
'''
import io
class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path
    def read_file(self):
        with io.open(self.file_path, "rb") as file:
            return file.read()
    def write_file(self, content):
        with io.open(self.file_path, "w", encoding="utf-8") as file:
            file.write(content)