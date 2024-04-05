from plates import is_valid

def main():
    test_letters()
    test_numbers()
    test_symbols()
    test_length()

def test_letters():
    assert is_valid("CS") == True
    assert is_valid("cs") == True
    assert is_valid("50") == False

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_symbols():
    assert is_valid("PI3.14") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS 50") == False

def test_length():
    assert is_valid("OUTATIME") == False
    assert is_valid("H") == False

if __name__ == "__main__":
    main()
