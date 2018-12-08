#reverse a string.. use recursion somehow

def revStr(string):
    if len(string) == 1:
        return string
    return string[len(string)-1] + revStr(string[0:(len(string)-1)])

def main():
    print('Will reverse "hello there".')
    stringg = 'hello there'
    print(revStr(stringg))

main()
