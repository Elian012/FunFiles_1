"""
 Author: Elian
 Purpose: Dir walk function.
 Date: 06.03.2024
"""
import os

from FunFiles_1.csv_reader import CsvReader
from FunFiles_1.file_reader import FileReader
from FunFiles_1.json_reader import JsonReader
from FunFiles_1.text_reader import TextReader


def dir_wallk(path):
    """
    Makes a list of FileReader objects.
    :param path: Dir path.
    :return: List of FileReader objects.
    """
    file_reader_list = []
    for filename in os.scandir(path):
        if filename.is_file():
            if is_file_reader_object(filename.path):
                file_reader_list.append(make_file_object(filename.path))
    return file_reader_list


def is_file_reader_object(file_path: str) -> bool:
    """
    Checks if the path is one of the three objects.
    :param file_path: File path.
    :return: True if it's a FileReader object.
    """
    file_extension = os.path.splitext(file_path)[1]
    return file_extension == ".txt" or file_extension == ".json" or file_extension == ".csv"


def make_file_object(file_path: str) -> FileReader:
    """
    Makes an object.
    :param file_path:
    :return: One of three objects that inherits from FileReader.
    """
    file_extension = os.path.splitext(file_path)[1]
    if file_extension == ".txt":
        return TextReader(file_path)
    elif file_extension == ".json":
        return JsonReader(file_path)
    elif file_extension == ".csv":
        return CsvReader(file_path)
