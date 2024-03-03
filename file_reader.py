import os.path
from abc import abstractmethod


class FileReader:
    def __init__(self, file_path):
        if os.path.isfile(file_path):
            self.file_path = file_path

    def size(self):
        return os.stat(self.file_path).st_size

    def name(self):
        return os.path.splitext(self.file_path)[0]
    
    @abstractmethod
    def read(self):
        pass
