#pascal's triangle, use recursion

def pascal(rows):
    if rows == 1:
        print(1)
        return
    else: print(1, end="")
    for row in range(1,rows):
        print("\n")
        for rowElem in range(row+1):
            res = calcCoef(row, rowElem)
            print("%d "%res, end="")

def calcCoef(row, rowElem):
    res = factorial(row) // (factorial(rowElem)*factorial(row-rowElem))
    return res

def factorial(num):
    if num == 0 or num == 1:
        return 1
    if num < 0:
        raise Exception("Can't factorial negative #!")
        
    return num * factorial(num-1)
    
    
