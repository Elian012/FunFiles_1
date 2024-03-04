from FunFiles_1.csv_reader import CsvReader
from FunFiles_1.text_reader import TextReader


def main():
    file_path_1 = r"C:\Users\USER\PycharmProjects\mailBox\mail_for_nati.txt"
    file_path_2 = r"C:\Users\USER\PycharmProjects\mailBox\work.csv"
    text_reader_check = TextReader(file_path_1)
    #text_reader_check.read()
    csv_reader_check = CsvReader(file_path_2)
    csv_reader_check.read()


if __name__ == '__main__':
    main()
