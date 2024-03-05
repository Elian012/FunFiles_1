"""
 Author: Elian
 Purpose: A csv file reader handler.
 Date: 04.03.2024
"""


def csv_read_handler(cell: str, numb_of_character: int) -> None:
    """
    Prints the cell in a specific way.
    :param cell: Cell of csv file.
    :param numb_of_character: Number of characters we want to print.
    """
    difference = numb_of_character - len(cell)
    if difference > 0:
        print(cell[:numb_of_character], end=f"{' ' * difference}| ")
    else:
        print(cell[:numb_of_character], end="| ")
