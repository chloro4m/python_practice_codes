#atoi and itoa problems
#dont use simple python conversions/cast(str)(int)
#use ord(char) to get ascii number

#atoi:
def atoi(s):
    #divide stringNum s into char pieces:
    charList = []
    for i in range(len(s)):
        charList.append(s[i])
    #convert chars to ints w/ ascii math
    intList = []
    for char in charList:
        intVal = ord(char) - ord('0')
        intList.append(intVal)
    #reverse list so the lowest 10s place is first in list
    intList.reverse()
    #do some math so we can add up to the proper final res
    res = 0
    multiplier = 1
    for num in intList:
        res += (num*multiplier)
        multiplier *= 10
    return res

print("atoi this string: 6900")
a = "6900"
print(atoi(a))
print("Adding 1 to result to make sure int math works:")
print(atoi(a) + 1)
print('\n')

#itoa:
def itoa(intt):
    #split the number into digits:
    digits = []
    num = intt
    while num != 0:
        digits.append(num %10)
        num = num // 10
    #make int digits in correct order, 1's place last elem
    digits.reverse()
    #convert each int to a char, then concatenate and return
    res = ""
    for intDigit in digits:
        res += str(intDigit)
    return res
    
print("itoa this int: 6900")
num = 6900
print("In a sentence strCat, the result is: " + itoa(num))
