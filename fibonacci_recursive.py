#compute Fibonacci recursively
#F-numbers:      0, 1, 1, 2, 3....
#Degree Values^: 0, 1, 2, 3, 4....

def fib(degree):
    global numcalls
    numcalls += 1
    if degree < 0:
        return 0
    if degree == 0:
        return 0
    if degree == 1:
        return 1
    return fib(degree - 1) + fib(degree - 2)
    
global numcalls
numcalls = 0

print("10th deg fib is: %d"%fib(10))
print("Numcalls to fib: %d"%numcalls)
