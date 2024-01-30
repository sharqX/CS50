def main():
    print("What is the Answer to the Great Question of Life, the Universe and Everything?")
    x = input()
    is_fortytwo(x)


def is_fortytwo(n):
    if n.strip() == "42":
        print("Yes")
    elif n.lower().strip() == "forty two":
        print("Yes")
    elif n.lower().strip() == "forty-two":
        print("Yes")
    else:
        print("No")

main()
