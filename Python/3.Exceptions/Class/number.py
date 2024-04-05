def main():
    x = get_int()
    print(f"s is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? ")) #return int(input("What's x? "))
        except ValueError:
            print("x is not an integer") #pass
        else:
            return x    #we can return the input in the same line itself shown above

main()


# def main():
#     x = get_int("What's x? ")
#     print(f"s is {x}")


# def get_int(promt):
#     while True:
#         try:
#             return int(input(promt))
#         except ValueError:
#             pass
#         
# main()