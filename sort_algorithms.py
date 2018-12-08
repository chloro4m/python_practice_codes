#here I AlexY will implement various sort algorithms

import random

#swap
def swap(listt, i, j):
    temp = listt[i]
    listt[i] = listt[j]
    listt[j] = temp

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
            
#selection sort (in-place)
def selection_sort(numList):
    length = len(numList)
    for i in range(length):
##        print('i = %d'%i) #debug
##        print('The list is currently: ' + str(numList)) #debug
        for j in range(i, length):
            if numList[j] < numList[i]:
                swap(numList, i, j)
    print(str(numList))
                
#bubble sort (in-place) (used recursion!!)
def bubble_sort(numList, start, end):
    if start == (end-1):
        return
    for i in range(end-1):
        if numList[i+1] < numList[i]:
            swap(numList, i, i+1)
    bubble_sort(numList, 0, end-1)

#insertion sort, only shifts elements
def insertion_sort(numList):
    length = len(numList)
    #starting from 2nd element, til end
    for i in range(1, length):
        curVal = numList[i]
        hole = i
        while i > 0:
            if numList[i-1] > curVal:
                #shift larger numbers right
                numList[i] = numList[i-1]
                hole = i-1
            i -= 1
        #after shift rights done, plug value into the hole
        numList[hole] = curVal
    print(str(numList))
                
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
    
def main():
    numList = [3, 2, 4, 5, 6, 7, 1, 9, -10, 7]
    print('Here\'s the list "numList" to sort:')
    print(str(numList))

    print('0. (Quit), 1. Selection, 2. Bubble, 3. Insertion, 4. Merge, 5. Quick') 
    choice = input('Enter which sort you want: ')
    if choice == '0':
        print('Nothing done.')
    elif choice == '1':
        print('Selection: ')
        selection_sort(numList)
    elif choice == '2':
        print('Bubble: ')
        bubble_sort(numList, 0, len(numList))
        print(str(numList))
    elif choice == '3':
        print("Insertion: ")
        insertion_sort(numList)
    elif choice == '4':
        print(merge_sort(numList))
    elif choice == '5':
        quick_sort(numList, 0, (len(numList)-1))
        print('Result: ')
        print(str(numList))
    else:
        print('Invalid choice.')

main()

#shellSort is basically insertion sort on gapped sublists of
#original list, then a final insertion sort
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

##alist = [54,26,93,17,77,31,44,55,20]
##print("alist for shell sort is initially: %s"%alist)
##shellSort(alist)
##print(alist)
