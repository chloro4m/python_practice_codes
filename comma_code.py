#This will take a list value and return all values as one string
#which is the list values comma-space separated, but includes 'and'
#between the last and 2nd to last items in the list

#function def
def listToStringPlus_and(listVal):
    endStr = str(listVal[0]) + ', '
    for i in range(1, len(listVal)):
        if i == (len(listVal) - 2):
            endStr += 'and '
        elif i == (len(listVal) - 1):
           endStr += str(listVal[i])
        else:
            endStr += str(listVal[i])
            endStr += ', '

    return endStr
    
#main
spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs', 'poop']
print(listToStringPlus_and(spam))

