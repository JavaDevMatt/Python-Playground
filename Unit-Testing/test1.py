# needs: pip install pytest
# run with: py.test *


from stuff_to_test import *

def test_return_stuff_string_positive():
    s = 'bla'
    assert return_stuff(s) == s

def test_return_stuff_string_negative():
    s = 'bla'
    assert return_stuff(s) != 'random other string'

def test_return_stuff_int_positive():
    d = 2
    assert return_stuff(d) == d
