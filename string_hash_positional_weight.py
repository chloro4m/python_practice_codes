#make string hash function w/ positional weights

def hash(astring, tablesize):
    weightedSum = 0
    for pos in range(len(astring)):
        weightedSum += ((pos + 1) * ord(astring[pos]))

    return weightedSum%tablesize

#using a different weighting scheme
    #pos**2 instead of pos
def hash2(astring, tablesize):
    weightedSum = 0
    for pos in range(len(astring)):
        weightedSum += ((pos**2) * ord(astring[pos]))

    return weightedSum%tablesize
