import csv
import sys
from tabulate import tabulate


def main():
    file = get_file()
    get_menu(file)


def get_file():
    file_name = sys.argv
    if len(file_name) > 2:
        sys.exit("Too many command-line arguments")
    if len(file_name) < 2:
        sys.exit("Too few command-line arguments")
    else:
        return file_name[1]


def get_menu(files):
    if files.endswith(".csv"):
        try:
            table = []
            with open(files) as file:
                reader = csv.reader(file)
                for row in reader:
                    table.append(row)
            print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
