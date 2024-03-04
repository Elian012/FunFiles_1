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
        difference = 0
        with open(self.file_path, 'r') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                for cell in row:
                    difference = numb_of_character - len(cell)
                    if difference > 0:
                        print(cell[:numb_of_character], end=f"{' ' * difference}| ")
                    else:
                        print(cell[:numb_of_character], end="| ")
                print()

