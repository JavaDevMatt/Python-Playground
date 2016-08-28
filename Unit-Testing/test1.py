#########################################################################################################
#   http://doc.pytest.org/en/latest/
#   needs: pip install pytest
#
#   run with: py.test *
#   or: pytest *
#   one function to test: pytest test1.py::test_return_stuff_int_positive
#
#########################################################################################################


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

def test_add_numbers():
    assert add_numbers(5, 15) == 20

# regex 
def test_phone_list_regex():
    s = 'My number is 415-555-4242. And here is another one 123-123-1234.'
    assert len(get_phone_numbers_list(s)) == 2
    assert get_phone_numbers_list(s)[0] == '415-555-4242'
    assert get_phone_numbers_list(s)[0] != 'bla'
    
