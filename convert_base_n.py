#this code will take a number in base 10 -> base n
#n=2:binary, etc..

def decToBin(number):
    print('Binary version of ' + str(number) + ':')
    result = []
    while number != 0:
        result.insert(0, str(number%2))
        number = number // 2
    x = ''.join(result)
    print(x)

def main():
    decToBin(5)
    decToBin(17)

main()
