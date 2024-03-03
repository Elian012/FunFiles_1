import os.path


class FileReader:
    def __init__(self, file_path):
        if os.path.isfile(file_path):
            self.file_path = file_path

