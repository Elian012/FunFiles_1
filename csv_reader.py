"""
 Author: Elian
 Purpose: A csv file reader.
 Date: 04.03.2024
"""
import csv

from FunFiles_1.file_reader import FileReader


class CsvReader(FileReader):
    """Csv file reader."""
    def read(self, numb_of_character: int = 5):
        """
        Prints every cell contact according to the max number of char in one column.
        :param numb_of_character: Number of character we want to print.
        """
        with open(self.file_path, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if len(row[0]) > numb_of_character:
                    print(row[0][:numb_of_character])
                else:
                    print(row[0])
