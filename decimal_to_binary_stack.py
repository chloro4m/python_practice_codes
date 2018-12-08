from pythonds.basic.stack import Stack

def decToBin(num):
    binStack = Stack()
    while num != 0:
        binDigit = num % 2
        binStack.push(binDigit)
        print("Pushed %d to stack"%binDigit)
        num = num // 2
    finalStr = ""
    while not binStack.isEmpty():
        finalStr = finalStr + str(binStack.pop())
    #return int(finalStr)
    return finalStr

print("Deci to Bin of 17: ")
print(decToBin(17))

print("Deci to Bin of 45: ")
print(decToBin(45))

print("Deci to Bin of 96: ")
print(decToBin(96))
