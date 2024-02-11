from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    # if square(2) !=4:
        # print("2 sqaured was not 4")
    assert square(3) == 9
    # if square(3) !=9:
        # print("3 sqaured was not 9")

if __name__=="__main__":
    main()