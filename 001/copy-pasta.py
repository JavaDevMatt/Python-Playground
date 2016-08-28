#An insecure copy pasta password locker program.

import pyperclip, sys

PASSWORDS = {'email': 'pass1',
             'blog': 'pass2'}

if len(sys.argv) < 2:
    print('Usage: python3 copy-pasta.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
