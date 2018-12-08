#write recursive factorial code

def factorialRecurs(num):
    if num == 1:
        return 1
    else:
        return (num * factorialRecurs(num-1))

    
