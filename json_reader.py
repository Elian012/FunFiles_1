"""
 Author: Elian
 Purpose: A json file reader class.
 Date: 05.03.2024
"""
import json

from FunFiles_1.file_reader import FileReader


class JsonReader(FileReader):
    """Json file reader."""
    def read(self):
        """
        Prints a list of keys of a Json file.
        """
        with open(self.file_path, 'r') as opened_file:
            file_data = json.load(opened_file)
        data_keys_lst = list(file_data.keys())
        print(data_keys_lst)
