from twttr import shorten

def main():
    test_vowels()
    test_numbers()
    test_symbols()

def test_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("tWItTer") == "tWtTr"

def test_numbers():
    assert shorten("123") == "123"
    assert shorten("Twitter21") == "Twttr21"

def test_symbols():
    assert shorten("~!@#$%^&*()_+=-`") == "~!@#$%^&*()_+=-`"
