#! python3

##Write a function named printTable() that takes a list of
##lists of strings and displays it in a well-organized table
##with each column right-justified. Assume that all the inner
##lists will contain the same number of strings. 

def printTable(listOfListsOfStrings):
    #below will get max string lengths per final printed column
    maxStrLengthsPerCol = []
    for i in range(0, len(listOfListsOfStrings)):
        strLength = 0
        for j in range(0, len(listOfListsOfStrings[0])):
            if (len(listOfListsOfStrings[i][j]) > strLength):
                strLength = len(listOfListsOfStrings[i][j])
        maxStrLengthsPerCol.append(strLength)
    #below will do the rjust() printing, adding 1 extra space
    for i in range(0, len(listOfListsOfStrings[0])): #len=4 (0,3)
        colNum = 0 
        for j in range(0, len(listOfListsOfStrings)): #len=3 (0,2)
            print(listOfListsOfStrings[j][i].\
                  rjust((1 + maxStrLengthsPerCol[colNum]), '*')\
                  , end='')
            colNum += 1
        print('\n')

    return maxStrLengthsPerCol

#main
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

debug = printTable(tableData)
