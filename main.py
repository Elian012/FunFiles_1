from FunFiles_1.text_reader import TextReader


def main():
    file_path_1 = r"C:\Users\USER\PycharmProjects\mailBox\mail_for_nati.txt"
    text_reader_check = TextReader(file_path_1)
    text_reader_check.read()


if __name__ == '__main__':
    main()
