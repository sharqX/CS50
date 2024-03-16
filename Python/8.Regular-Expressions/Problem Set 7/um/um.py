import re

def main():
    print(count(input("Text: ")))

def count(s):
    for i in range(len(s)):
        a = re.findall(r"\bum\b", s, re.IGNORECASE)
        break

    return len(a)

if __name__ == "__main__":
    main()
