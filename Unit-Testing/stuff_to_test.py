def return_stuff(a):
    return a

def add_numbers(a, b):
    return a + b

import re

def get_phone_numbers_list(s):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    return phoneNumRegex.findall(s)
