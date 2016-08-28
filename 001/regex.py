import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phone_list = phoneNumRegex.findall('My number is 415-555-4242. And here is another one 123-123-1234.')

if len(phone_list) > 0:
    print('Phone numbers found: ')
else:
    print('No phone numbers found')
for index in phone_list:
    print(index)
