#quicksort_with_insertion_for_smaller_lists
#do some benchmarking
import time
import random

#swap
def swap(listt, i, j):
    temp = listt[i]
    listt[i] = listt[j]
    listt[j] = temp

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
   ## print('debug: '+str(numList))
    #partitionQuickSort selects a pivot and rearranges values
    if start < end:
        idx = partitionQuickSort(numList, start, end)
        quick_sort(numList, start, idx-1)
        quick_sort(numList, idx+1, end)
    return

#insertion sort, only shifts elements
def insertion_sort(numList):
    length = len(numList)
    #starting from 2nd element, til end
    for i in range(1, length):
      ##  print("Current list: %s"%numList)
        curVal = numList[i]
        hole = i
      ##  print("Hole index: %d"%hole)
        while i > 0:
            if numList[i-1] > curVal:
                #shift larger numbers right
                numList[i] = numList[i-1]
                hole = i-1
          ##      print(numList)
            ##    print("Hole index changed: %d"%hole)
            i -= 1
        #after shift rights done, plug value into the hole
        numList[hole] = curVal
 ##   print(str(numList))
 ##   print("Done\n")


#initialize small and large lists

randList15 = []
for i in range(15):
    randList15.append(random.randrange(-100, 100))
##print("Here is rand list of 15:")
##print(randList15)

randList1000 = []
for i in range(1000):
    randList1000.append(random.randrange(-100, 100))
##print("Here's rand list of 1000:")
##print(randList1000)

#run benchmark on 15 list
    #insertion
begin = time.time()
for i in range(1000):
    L = randList15[:]
    insertion_sort(L)
end = time.time()
print("Insertion sort 1000x on random list of 15 took (sec):")
print(end-begin)
    #quick
begin = time.time()
for i in range(1000):
    L = randList15[:]
    quick_sort(L, 0, 14)
end = time.time()
print("Quick sort 1000x on random list of 15 took (sec):")
print(end-begin)

#run benchmark on 1000 list
    #insertion
begin = time.time()
for i in range(50):
    L = randList1000[:]
    insertion_sort(L)
end = time.time()
print("Insertion sort 50x on random list of 1000 took (sec):")
print(end-begin)
    #quick
begin = time.time()
for i in range(50):
    L = randList1000[:]
    quick_sort(L, 0, 999)
end = time.time()
print("Quick sort 50x on random list of 1000 took (sec):")
print(end-begin)
