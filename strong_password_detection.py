##Regex check password:
##at least eight characters long,
##contains both uppercase and lowercase characters,
##and has at least one digit

import re
pwRgx = re.compile(r'(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)(\S){8,}')

print('Password must be at least 8 characters long, \
have both upper and lowercase, and at least one digit.\
 No special symbols allowed. \
Use only from [0-9][a-z][A-Z].\n')
print('Will try 5 separate rounds:\n')

for i in range (0,5):
    print('(Round ' + str(i+1) + '). ' + 'Please enter a password: ')
    pw = input()

    matchObj = pwRgx.search(pw)
    if (matchObj == None):
        print('Password not strong enough!!!\n')
    else:
        print('We received: ' + matchObj.group())
        print('This is strong enough. Good job!!!\n')
        
