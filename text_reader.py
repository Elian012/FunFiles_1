"""
 Author: Elian
 Purpose: A text file reader class.
 Date: 04.03.2024
"""
from FunFiles_1.file_reader import FileReader


class TextReader(FileReader):
    """A text file reader."""
    def read(self):
        """
        Prints the file's content.
        """
        with open(self.file_path, "r") as opened_file:
            file_text = opened_file.read()

        print(file_text)

