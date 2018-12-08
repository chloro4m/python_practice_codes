#show how random list is sorted by:
##bubble sort
##selection sort
##insertion sort
##shell sort (you decide on the increments)
##merge sort
##quick sort (you decide on the pivot value)
import random

oneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tenToOne = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
numList = [3, 2, 4, 5, 6, 7, 1, 9, -10, 7]
#print('Here\'s the list "numList" to sort:')
#print(numList)

#swap
def swap(listt, i, j):
    temp = listt[i]
    listt[i] = listt[j]
    listt[j] = temp

#bubble sort (in-place) (used recursion!!)
def bubble_sort(numList, start, end):
    print("Current state of list: %s"%numList)
    if start == (end-1):
        return
    for i in range(end-1):
        if numList[i+1] < numList[i]:
            swap(numList, i, i+1)
            print("Current state of list: %s"%numList)
    bubble_sort(numList, 0, end-1)

##bubble_sort(numList, 0, len(numList))
##print("\nSort from starting with: %s"%oneToTen)
##bubble_sort(oneToTen, 0, len(numList))
##print("\nSort from starting with: %s"%tenToOne)
##bubble_sort(tenToOne, 0, len(numList))

#selection sort (in-place)
def selection_sort(numList):
    length = len(numList)
    for i in range(length):
        print('The list is currently: ' + str(numList)) #debug
        for j in range(i, length):
            if numList[j] < numList[i]:
                swap(numList, i, j)
                print('The list is currently: ' + str(numList))
    print(str(numList))

##selection_sort(numList)
##selection_sort(oneToTen)
##selection_sort(tenToOne)

#insertion sort, only shifts elements
def insertion_sort(numList):
    length = len(numList)
    #starting from 2nd element, til end
    for i in range(1, length):
        print("Current list: %s"%numList)
        curVal = numList[i]
        hole = i
        print("Hole index: %d"%hole)
        while i > 0:
            if numList[i-1] > curVal:
                #shift larger numbers right
                numList[i] = numList[i-1]
                hole = i-1
                print(numList)
                print("Hole index changed: %d"%hole)
            i -= 1
        #after shift rights done, plug value into the hole
        numList[hole] = curVal
    print(str(numList))
    print("Done\n")

##insertion_sort(numList)
##insertion_sort(oneToTen)
##insertion_sort(tenToOne)

#join, for merge sort, returns one sorted list; assume A & B sorted
def joinMergeSort(listA, listB):
    res = []
    a = len(listA)
    b = len(listB)
    x = 0
    y = 0
    while x < a and y < b:
        if listA[x] <= listB[y]:
            res.append(listA[x])
            x += 1
        else:
            res.append(listB[y])
            y += 1
    #loop to fill leftover list to res, enters only one below
    while x < a:
        res.append(listA[x])
        x += 1
    while y < b:
        res.append(listB[y])
        y += 1
        
    return res   

#merge sort O(n log n)
def merge_sort(numList):
    length = len(numList)
    #base case
    if length == 1:
        print('debug: hit base case')
        return numList

    else:
        mid = length//2
        #left split
        left = []
        for i in range(0, mid):
            left.append(numList[i])
        print('debug: intermediate left list value '+str(left))
        #right split
        right = []
        for i in range(mid, length):
            right.append(numList[i])
        print('debug: intermediate right list value '+str(right))
        #recursive call to L and R
        ##print('debug: about to merge_sort left')
        leftt = merge_sort(left)
        ##print('debug: about to merge_sort right')
        rightt = merge_sort(right)
        #now we need logic to join+sort 2 lists into 1
    final = joinMergeSort(leftt, rightt)
    return final

##print("\nRandom list:")
##x = merge_sort(numList)
##print(x)
##print("\noneToTen list:")
##x = merge_sort(oneToTen)
##print(x)
##print("\ntenToOne list:")
##x = merge_sort(tenToOne)
##print(x)

#partition for QS, should return pIdx
def partitionQuickSort(numList, start, end):
    pivotInitIdx = random.randrange(start, end+1)
    pivotVal = numList[pivotInitIdx] #choosing pivot
    swap(numList, pivotInitIdx, end) #move pivot to end of list for simplicity
    pIdx = start
    for i in range(start, end):
        if numList[i] <= pivotVal:
            swap(numList, i, pIdx)
            pIdx += 1
    swap(numList, pIdx, end)
    return pIdx
        
#quick sort (generally best, in-place)
def quick_sort(numList, start, end):
    #debug
    print('debug: '+str(numList))
    #partitionQuickSort selects a pivot and rearranges values
    if start < end:
        idx = partitionQuickSort(numList, start, end)
        quick_sort(numList, start, idx-1)
        quick_sort(numList, idx+1, end)
    return

print("\nRandom list:")
quick_sort(numList, 0, len(numList)-1)
print("\noneToTen list:")
quick_sort(oneToTen, 0, len(oneToTen)-1)
print("\ntenToOne list:")
quick_sort(tenToOne, 0, len(tenToOne)-1)
