"""
 Author: Elian
 Purpose: A file reader.
 Date: 03.03.2024
"""
import os.path
from abc import abstractmethod


class FileReader:
    """A file reader."""
    def __init__(self, file_path):
        if os.path.isfile(file_path):
            self.file_path = file_path

    def size(self):
        """
        Returns the file's size.
        :return: The file size.
        """
        return os.stat(self.file_path).st_size

    def name(self):
        """
        Return the file name.
        :return: File name.
        """
        return os.path.splitext(self.file_path)[0]
    
    @abstractmethod
    def read(self):
        """Abstract method."""
        pass
