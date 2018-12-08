#fibonacci with memoization / pseudo?-dynamic program

#F-numbers:      0, 1, 1, 2, 3....
#Degree Values^: 0, 1, 2, 3, 4....

def fib(degree):
    memo = {0:0, 1:1}
    return fib1(degree, memo)

def fib1(degree, memo):
    global numcalls
    numcalls += 1
    if degree in memo:
        return memo[degree]
    else:
        memo[degree] = fib1(degree-1, memo) + fib1(degree-2, memo)
    return memo[degree]

global numcalls
numcalls = 0

print("10th deg fib is: %d"%fib(10))
print("Numcalls to fib1: %d"%numcalls)
