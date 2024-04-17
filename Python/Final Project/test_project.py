import pytest
from project import Pomodoro

pmd = Pomodoro()

def test_menu():
    with pytest.raises(ValueError):
        pmd.test_menu("cat")
    with pytest.raises(ValueError):
        pmd.test_menu(3)

def test_conti():
    with pytest.raises(ValueError):
        pmd.test_conti("CS50")
    with pytest.raises(ValueError):
        pmd.test_conti(5)

def test_settings():
    with pytest.raises(ValueError):
        pmd.test_settings("zero","five","vf","one","a","b")
    with pytest.raises(ValueError):
        pmd.test_settings("","","","","","")