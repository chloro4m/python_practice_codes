#recursion to reverse list

##def reverse(lst):
##    if not lst: # this will be true if lst == []
##        return lst
##    return lst[-1:] + reverse(lst[:-1]) # recursive case
##
### Demo
##print(reverse([1,2,3,4,5])) # [5, 4, 3, 2, 1]
        
def rev(aList):
    if len(aList) == 0:
        return aList
    else:
        return [aList[-1]] + rev(aList[:-1])
