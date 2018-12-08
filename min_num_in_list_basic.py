##Write two Python functions to find the minimum number in a list.
##The first function should compare each number to every other number on the list. O(n2).
##The second function should be linear O(n).

def bigO_nSquared(listt):
    minim = listt[0]
    for i in range(len(listt)):
        for j in range(len(listt)):
            if listt[i] < listt[j]:
                if listt[i] < minim:
                    minim = listt[i]
    print('The smallest with O(n^2) is %d.' %minim)
    return      

def bigO_n(listt):
    minim = listt[0]
    for i in range(len(listt)):
        if listt[i] < minim:
            minim = listt[i]
    print('The smallest with O(n) is %d.' %minim)
    return                

def main():
    listt = []
    print('Enter list of 5 numbers, we\'ll find the smallest.')
    for i in range(5):
        listt.append(int(input()))

    print('Here is your list:')
    print(listt)

    bigO_nSquared(listt)

    bigO_n(listt)

main()
