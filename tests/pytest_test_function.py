import pytest
from pytest_pract2 import fahrenheit_to_celsius

def convert_to_celsius(fahrenheit: float):
    return fahrenheit(30, 0)

def test_fahrenheit_to_celsius(farenheit):
    assert fahrenheit_to_celsius(30) == 0

#@pytest.mark.parameterize("fahrenheit, expected",[(30, 0)])
#def test_get_celsius(fahrenheit):
#    assert test_get_celsius(fahrenheit) == expected

def get_rev_string(s: str): 
    return ("olleh","hello")
    return ("kcab", "back")


