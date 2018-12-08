#recursively detect if word is palindrome

def isPal(string):
    #base case
    if len(string) <= 2:
        if string[0] == string[-1]:
            return True
        else:
            return False
    #condition
    if string[0] == string[-1]:
        return True
    else:
        return False
    #recurse
    return isPal(string[1:(len(string)-1)]) and True

def stripSpcPnc(string): #also add toLower
    newStr = ''
    for char in string:
        if char.isalpha():
            newStr += char.lower()
    return newStr

def main():
    print('Detecting if "poop" is palindrome: ')
    s1 = 'poop'
    print(isPal(s1))
    print('How bout "Go hang a salami; I’m a lasagna hog.": ')
    s2 = 'Go hang a salami; I’m a lasagna hog.'
    #strip white space and punct. and toLower
    s2x = stripSpcPnc(s2)
    print(isPal(s2x))
    print('How bout a negative case "fecku": ')
    s3 = 'fecku'
    print(isPal(s3))

main()
