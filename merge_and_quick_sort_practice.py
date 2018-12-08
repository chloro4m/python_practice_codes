#need to have merge and quick sort down by heart

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = []
        for i in range(0, mid):
            left.append(arr[i])
        right = []
        for j in range(mid, len(arr)):
            right.append(arr[j])
        leftt = mergeSort(left)
        rightt = mergeSort(right)
    final = mergeHelp(leftt, rightt)
    return final

def mergeHelp(arrA, arrB): #returns sorted array
    a = len(arrA)
    b = len(arrB)
    x = 0
    y = 0
    merged = []
    while x < a and y < b:
        if arrA[x] < arrB[y]:
            merged.append(arrA[x])
            x += 1
        else:
            merged.append(arrB[y])
            y += 1
    #flush out the remainder from either just presorted A or B
    while x < a:
        merged.append(arrA[x])
        x += 1
    while y < b:
        merged.append(arrB[y])
        y += 1
    return merged

#------------------------------------------------------------
import random

def quickSort(arr):
    startIdx = 0
    endIdx = len(arr)-1
    quickSortHelp(arr, startIdx, endIdx)

def quickSortHelp(arr, start, end):
    if start < end:
        pIdx = partitionHelp(arr, start, end)
        quickSortHelp(arr, start, pIdx-1)
        quickSortHelp(arr, pIdx+1, end)
    return
    
def partitionHelp(arr, start, end): #returns partIdx
    if start == end:
        return
    else:
        randPivotIdx = random.randrange(start, end+1)
        pivotVal = arr[randPivotIdx]
        swap(arr, end, randPivotIdx) #move pivot to end for simp.
        pIdx = start
        for i in range(start, end):
            if arr[i] < pivotVal:
                swap(arr, i, pIdx)
                pIdx += 1
        swap(arr, pIdx, end) #move pivot from end to pIdx
        return pIdx

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    
x = [3, 2, 4, 5, 6, 7, 1, 9, -10, 7]
y = [54,26,93,17,77,31,44,55,20]
