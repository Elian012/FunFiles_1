from FunFiles_1.csv_reader import CsvReader
from FunFiles_1.dir_walk_func import dir_wallk
from FunFiles_1.text_reader import TextReader


def main():
    file_reader_list = dir_wallk(r"C:\Users\USER\PycharmProjects\FunFiles\FunFiles_1")
    for file_read_object in file_reader_list:
        if file_read_object.size() < 1000000:
            file_read_object.read()
            print()


if __name__ == '__main__':
    main()
