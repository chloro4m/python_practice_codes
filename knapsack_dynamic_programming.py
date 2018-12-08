#4.14 NOT DONE!
#knapsack problem (max value), use dynamic programming
#sack holds W=20 weight of art
#sample problem:
#item:   1  2  3  4  5
#weight: 2  3  4  5  9
#value:  3  4  8  8  10


#def maxVal(wtList, valList, idx, remainWt):
def maxVal(wtList, valList, idx, remainWt, memo):

    global numcalls
    numcalls += 1
    print("maxVal called with idx: %d, remainWt: %d"%(idx, remainWt))

    ##check memo, this code *should* be right
    if (idx, remainWt) in memo:
        return memo[(idx, remainWt)]
    
    ##base case at last idx (0) either take or cant take due to weight
    if idx == 0:
        if wtList[0] <= remainWt:
            return valList[0]
        else:
            return 0

    #dontTakePath = maxVal(wtList, valList, idx-1, remainWt) 
    dontTakePath = maxVal(wtList, valList, idx-1, remainWt, memo)
    
    if wtList[idx] <= remainWt:
        remainWt -= wtList[idx]
    else:
        return 0
    #takePath = v[idx] + maxVal(wtList, valList, idx-1, remainWt)
    takePath = v[idx] + maxVal(wtList, valList, idx-1, remainWt, memo)
    
    #return max(takePath, dontTakePath)
    memo[(idx, remainWt)] = max(takePath, dontTakePath)
    return memo[(idx, remainWt)]

##main call, sack is 20 W big

##w = [2, 3, 4, 5, 9]
##v = [3, 4, 8, 8, 10]
##W = 20

##w = [5, 4, 6, 3]
##v = [10, 40, 30, 50]
##W = 10

w = [3, 2, 4, 1]
v = [100, 20, 60, 40]
W = 5


cache = {} ##keys as such: (idx, remainWt):finalVal

global numcalls
numcalls = 0

knapsackVal = maxVal(w, v, len(w)-1, W, cache)
#knapsackVal = maxVal(w, v, len(w)-1, 20)

print("Answer is %d"%knapsackVal)
print("Total numcalls: %d"%numcalls)
        


    
