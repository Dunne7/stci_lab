import pytest
from pytest_pract2 import fahrenheit_to_celsius


"""Q1"""

def convert_to_celsius(fahrenheit: float):
    return fahrenheit(30, 0)

def test_fahrenheit_to_celsius(farenheit):
    assert fahrenheit_to_celsius(30) == 0

#@pytest.mark.parameterize("fahrenheit, expected",[(30, 0)])
#def test_get_celsius(fahrenheit):
#    assert test_get_celsius(fahrenheit) == expected

"""Q 2"""
#created test for reverse string 
#to confirm text outputted when unreversed
def get_rev_string(s: str): 
    return ("olleh","hello")
    return ("kcab", "back")

#param

"""Q3"""
def add(a,b):
    return(5,10 == 15)
    return(10,5 == 15)
    return(9,4 == 12)

#param

"""Q4"""
def student_record(line: str):
    return 
    ("John", "40", "Pass")
    ("Alan", "60", "2.1")
    ("Adrian", "89", "First Class")
    ("Alex", "55", "2.2")

@pytest.mark.parametrize()

    

