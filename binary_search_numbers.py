#tasking myself to write a binary sort
#for list of numbers. use recursion!

def binSearch(listt, num):
    #base case:
    if len(listt) == 1:
        if listt[0] == num:
            return True
        else:
            return False
        
    mid = len(listt)//2
    if listt[mid] == num:
        return True
    elif num < listt[mid]:
        return binSearch(listt[:mid], num)
    elif num > listt[mid]:
        return binSearch(listt[mid+1:], num)


def main():
    newList = [123, 123, 4, 34, 56, 1, 6856, -30, 324]
    newList.sort()
    print('Binary search on sorted newList:')
    print(newList)
    print('Is 4 in the list?: ')
    print(binSearch(newList, 4))
    print('Is 69 in it?: ')
    print(binSearch(newList, 69))

main()
