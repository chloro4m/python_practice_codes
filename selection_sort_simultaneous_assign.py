#selection sort with simult. assign.

#selection sort (in-place)
def selection_sort(numList):
    length = len(numList)
    for i in range(length):
        print('The list is currently: ' + str(numList)) #debug
        for j in range(i, length):
            if numList[j] < numList[i]:
                numList[i], numList[j] = numList[j], numList[i]
                print('The list is currently: ' + str(numList))
    print(str(numList))


oneToTen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tenToOne = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
numList = [3, 2, 4, 5, 6, 7, 1, 9, -10, 7]

selection_sort(numList)
selection_sort(oneToTen)
selection_sort(tenToOne)
