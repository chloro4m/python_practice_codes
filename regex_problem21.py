


import re

nameRgx = re.compile(r'[A-Z][a-z]*(\sNakamoto)$')

print('Matches:')
###
print('Satoshi Nakamoto')
matchObj = nameRgx.search('Satoshi Nakamoto')
print(matchObj.group())

print('Alice Nakamoto')
matchObj = nameRgx.search('Alice Nakamoto')
print(matchObj.group())

print('Robocop Nakamoto')
matchObj = nameRgx.search('Robocop Nakamoto')
print(matchObj.group())

print('Should not match:')
###
print('satoshi Nakamoto')
matchObj = nameRgx.search('satoshi Nakamoto')
print(matchObj.group())

print('Mr. Nakamoto')
matchObj = nameRgx.search('Mr. Nakamoto')
print(matchObj.group())

print('Nakamoto')
matchObj = nameRgx.search('Nakamoto')
print(matchObj.group())

print('Satoshi nakamoto')
matchObj = nameRgx.search('Satoshi nakamoto')
print(matchObj.group())
