#! python3

#pw.py - Insecure password locker

PASSWORDS = {'email': 'email69', 'blog': 'blog69', 'luggage': \
             'luggage 69'}

import sys
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy acc pw')
    sys.exit()

account = sys.argv[1] #first cmd line arg is acc name

import pyperclip

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no acc named ' + account)
    
