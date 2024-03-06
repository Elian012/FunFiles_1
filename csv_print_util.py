"""
 Author: Elian
 Purpose: A csv file reader handler.
 Date: 04.03.2024
"""


def cell_print_handler(cell: str, num_char_to_print: int) -> None:
    """
    Prints the cell in a specific way.
    :param cell: Cell of csv file.
    :param num_char_to_print: Number of characters we want to print.
    """
    difference = num_char_to_print - len(cell)
    if difference > 0:
        print(cell[:num_char_to_print], end=f"{' ' * difference}| ")
    else:
        print(cell[:num_char_to_print], end="| ")
