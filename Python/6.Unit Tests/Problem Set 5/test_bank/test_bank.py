from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()

def test_zero():
    assert value("hello") == 0
    assert value("HeLlO") == 0

def test_twenty():
    assert value("h") == 20
    assert value("Hey") == 20

def test_hundred():
    assert value("whats up") == 100
    assert value("WHATS UP") == 100
    assert value("What's Up?") == 100
    assert value("123") == 100
    assert value("!@#$%^&*()_+=-`") == 100

if __name__ == "__main__":
    main()
