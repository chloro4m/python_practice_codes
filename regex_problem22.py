##-Regex that matches a sentence where the first word
##is either Alice, Bob, or Carol; the second word is
##either eats, pets, or throws; the third word
##is apples, cats, or baseballs;
##and the sentence ends with a period?
##This regex should be case-insensitive.


import re
rgx = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples\.|cats\.|baseballs\.)', re.IGNORECASE)

print('Matches:')
mo = rgx.search('Alice eats apples.')
print(mo.group())
mo = rgx.search('Bob pets cats.')
print(mo.group())
mo = rgx.search('Carol throws baseballs.')
print(mo.group())
mo = rgx.search('Alice throws Apples.')
print(mo.group())
mo = rgx.search('BOB EATS CATS.')
print(mo.group())

print('Doesnt match (should print None after each line):')
print('Robocop eats apples.')
mo = rgx.search('Robocop eats apples.')            
print(mo)               
print('ALICE THROWS FOOTBALLS.')
mo = rgx.search('ALICE THROWS FOOTBALLS.')            
print(mo)  
print('Carol eats 7 cats.')
mo = rgx.search('Carol eats 7 cats.')            
print(mo)  
