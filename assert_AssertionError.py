#Write an assert statement that triggers an AssertionError
#if the variable spam is an integer less than 10.

spam = 10
print('spam set to 10')

assert int(spam) >= 10, 'Problem if spam is int < 10'

spam = 9.69
print('now set to 9.69')

assert int(spam) >= 10, 'Problem if spam is int < 10'


