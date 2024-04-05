import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"<iframe(.)*></iframe>", s):
        if url := re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)", s, re.IGNORECASE):
            id = url.groups()
            return "https://youtu.be/" + id[0]

if __name__ == "__main__":
    main()
