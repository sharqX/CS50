import csv
import sys


def main():
    read, write = get_file()
    clean_file(read, write)


def get_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        readFile = sys.argv[1]
        writeFile = sys.argv[2]
        if readFile.endswith(".csv") and writeFile.endswith(".csv"):
            return readFile, writeFile


def clean_file(read, write):
    with open(read) as before:
        reader = csv.DictReader(before)
        with open(write, "w") as after:
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writerow({"first": "first", "last": "last", "house": "house"})
            for row in reader:
                last, first = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first": first, "last": last, "house": house})

if __name__ == "__main__":
    main()
