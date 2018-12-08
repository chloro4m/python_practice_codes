import random

def quickSort(arr):
    lastIdx = len(arr) - 1
    quickSortHelp(arr, 0, lastIdx)

def swap(arr, idx1, idx2):
    temp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = temp

def quickSortHelp(arr, start, end):
    print("Start: %d, End: %d"%(start, end))
    if end < start:
        return
    else:
        pIdx = partition(arr, start, end)
        print("pIdx: %d"%pIdx)
        quickSortHelp(arr, start, pIdx-1)
        quickSortHelp(arr, pIdx+1, end)
        return

def partition(arr, start, end):
    print("Inside partition, Start: %d, End: %d"%(start, end))
    randPivotIdx = random.randrange(start, end+1)
    pivotVal = arr[randPivotIdx]
    swap(arr, end, randPivotIdx)
    pivotIdx = start
    for i in range(start, end):
        if arr[i] < pivotVal:
            swap(arr, i, pivotIdx)
            pivotIdx += 1
    swap(arr, pivotIdx, end)
    return pivotIdx

arr = [5, 4, 3, 2, 1]
quickSort(arr)
print(arr)
