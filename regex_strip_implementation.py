##Write a function that takes a string and
##does the same thing as the strip() string method.
##If no other arguments are passed other than the string to strip,
##then whitespace characters will be removed
##from the beginning and end of the string.
##Otherwise, the characters specified in the second
##argument to the function will be removed from the string.

import re

def rgxStrip(string, stripVal=''):
    if stripVal == '':
        #regex to remove white space
        rgx_white = re.compile(r'\w+')
        #return whitespace-stripped
        mObj_white = rgx_white.search(string)
        print(mObj_white.group())
        return mObj_white.group()
    else:
        #regex to undo the stripVal from the ends
        rgx_strip = re.compile('[^'+stripVal+']' +r'(\w+)'+ '[^'+stripVal+']')
        mObj_strip = rgx_strip.search(string)
        print(mObj_strip.group())
        return mObj_strip.group()


#main
print("Call the function like this (use 'string' format)to strip(): \
rgxStrip(string, stripVal)")
