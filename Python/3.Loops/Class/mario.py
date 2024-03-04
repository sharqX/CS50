def main():
    # print_column(3)
    # print_rows(4)
    print_sqaure(50000000000)

# def print_column(height):
#     for _ in range(height):
#         print("#")

# def print_rows(width):
        # print("?" * width)

def print_sqaure(size):
     for i in range(size):
        for j in range(size):
            print("[]", end="")
        print()

main()
