import re


def return_stuff(a):
    return a


def add_numbers(a, b):
    return a + b


def get_phone_numbers_list(s):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    return phoneNumRegex.findall(s)
