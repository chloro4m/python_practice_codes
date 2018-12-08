##A bubble sort can be modified to “bubble” in both
##directions. The first pass moves “up” the list, and
##the second pass moves “down.” This alternating pattern
##continues until no more passes are necessary.

def bubble_sort_2way(numList, start, end):
    #not done
    print("Current state of list: %s"%numList)
    if start == (end-1):
        return
    
    anySwaps = False

    #first pass to bubble "up" list
    for i in range(end-1):
        if numList[i+1] < numList[i]:
            anySwaps = True
            numList[i+1], numList[i] = numList[i], numList[i+1]
            print("Current state of list (up): %s"%numList)

    #secone pass to bubble "down" list
    for j in range(end-1, 0, -1):
        if numList[j-1] > numList[j]:
            anySwaps = True
            numList[j], numList[j-1] = numList[j-1], numList[j]
            print("Current state of list(down): %s"%numList)

    if anySwaps == False:
        print("No swaps on this pass, so done sorting.")
        return
    else:
        bubble_sort_2way(numList, 0, end-1)


oneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tenToOne = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
numList = [3, 2, 4, 5, 6, 7, 1, 9, -10, 7]

bubble_sort_2way(numList, 0, len(numList))
print("\nSort from starting with: %s"%oneToTen)
bubble_sort_2way(oneToTen, 0, len(numList))
print("\nSort from starting with: %s"%tenToOne)
bubble_sort_2way(tenToOne, 0, len(numList))
