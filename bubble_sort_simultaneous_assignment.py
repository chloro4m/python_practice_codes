#bubble sort with simultaneous assignment
# ex) a, b = b, a

#bubble sort (in-place) (used recursion!!)
def bubble_sort(numList, start, end):
    print("Current state of list: %s"%numList)
    if start == (end-1):
        return
    for i in range(end-1):
        if numList[i+1] < numList[i]:
            numList[i+1], numList[i] = numList[i], numList[i+1]
            print("Current state of list: %s"%numList)
    bubble_sort(numList, 0, end-1)


oneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tenToOne = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
numList = [3, 2, 4, 5, 6, 7, 1, 9, -10, 7]

bubble_sort(numList, 0, len(numList))
print("\nSort from starting with: %s"%oneToTen)
bubble_sort(oneToTen, 0, len(numList))
print("\nSort from starting with: %s"%tenToOne)
bubble_sort(tenToOne, 0, len(numList))
