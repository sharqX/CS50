from datetime import date
import inflect
import sys
import operator

p = inflect.engine()


def main():
    birthday = input("Date of Birth: ")
    format(birthday)

def format(y):
     try:
        diff = operator.sub(date.today(), date.fromisoformat(y))
        print(mins(int(diff.days)))
     except:
        sys.exit("Invalid Date")

def mins(x):
    min = x * 24 * 60
    return f"{p.number_to_words(min, andword='').capitalize()} minutes"

if __name__ == "__main__":
    main()
