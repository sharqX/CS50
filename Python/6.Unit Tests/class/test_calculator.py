from calculator import square

def main():
    test_square()

def test_square():  
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 sqaured was not 4")
    # if square(2) !=4:
        # print("2 sqaured was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 sqaured was not 9")
    # if square(3) !=9:
        # print("3 sqaured was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 sqaured was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 sqaured was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 sqaured was not 0")

if __name__=="__main__":
    main()