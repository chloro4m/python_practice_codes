#Collatz sequence#

#function defs

def collatz(number):
    result = 0
    numInt = int(number)
    if isEven(numInt):
        print(str(numInt // 2))
        return numInt // 2
    elif isOdd(numInt): 
        print(str(3*numInt +1))
        return 3*numInt +1
    else:
        print('Error occurred, check input?!')


def isEven(x):
    if (x % 2 == 0):
        return True
    else:
        return False


def isOdd(x):
    if (x % 2 == 1):
        return True
    else:
        return False

#main program
print('Please input a number. We will play this 6 times.')
print('If number is even, then collatz() should print number // 2 and return this value.')
print('If number is odd, then collatz() should print and return 3 * number + 1.')
for i in range (0,6):
    print('Input number now.', end='--->')
    inputNum = input()
    collatz(inputNum)
