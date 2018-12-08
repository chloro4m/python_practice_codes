##How would you write a regex that matches a \
##number with commas for every three digits? \
##It must match the following:
##
##'42'
##
##'1,234'
##
##'6,368,745'
##
##but not the following:
##
##'12,34,567' (which has only two digits between the commas)
##
##'1234' (which lacks commas)

import re

numRgx = re.compile(r'^(\d\d\d,|\d\d\d|\d\d|\d)(,\d\d\d)*$')

#accept: 1 11 111 or 111,
#reject: 1111 ,1 11, 

print('result of entered 42:')
mo = numRgx.search('42')
print(mo.group())

print('result of entered 1,234:')
mo = numRgx.search('1,234')
print(mo.group())

print('result of entered 6,368,745:')
mo = numRgx.search('6,368,745')
print(mo.group())

print('result of entered 12,34,567:')
mo = numRgx.search('12,34,567')
print(mo.group())

print('result of entered 1234:')
mo = numRgx.search('1234')
print(mo.group())

