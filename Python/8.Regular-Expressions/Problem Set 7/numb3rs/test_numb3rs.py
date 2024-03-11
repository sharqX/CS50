from numb3rs import validate

def test_format():
    assert validate("1.1.1.1") == True
    assert validate("8.8.8") == False
    assert validate("512.512.512.512") == False
    assert validate("0") == False
    assert validate("cat") == False


def test_ip():
    assert validate("172.0.0.1") == True
    assert validate("512.1.1.1") == False
    assert validate("1.512.1.1") == False
    assert validate("1.1.512.1") == False
    assert validate("1.1.1.512") == False
