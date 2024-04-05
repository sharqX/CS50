import seasons
import pytest

def test_format():
    with pytest.raises(SystemExit):
        seasons.format("24 June 1999")

def test_mins():
    assert seasons.mins(9043) == "Thirteen million, twenty-one thousand, nine hundred twenty minutes"
