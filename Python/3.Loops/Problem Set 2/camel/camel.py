def main():
    camelCase = input("camelCase: ")
    snake_case(camelCase)


def snake_case(name):
    for c in name:
        if c.isupper():
            print("_" + c.lower(), end="")
        else:
            print(c, end="")
    print()


main()
