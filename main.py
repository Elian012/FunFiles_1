"""
 Author: Elian
 Purpose: Runs on a list of objects and print the files.
 Date: 07.03.2024
"""
from FunFiles_1.dir_walk_func import dir_wallk

ONE_MEGA_BYTE = 1000000


def main():
    """Entry point"""
    file_reader_list = dir_wallk(r"C:\Users\USER\PycharmProjects\FunFiles\FunFiles_1")
    for file_read_object in file_reader_list:
        if file_read_object.size() < ONE_MEGA_BYTE:
            file_read_object.read()
            print()


if __name__ == '__main__':
    main()
