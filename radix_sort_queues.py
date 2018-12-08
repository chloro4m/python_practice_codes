#implement radix sort machine
#main bin, 0-9 bins, all queues

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def radixSort(numList):
    #main bin with all number initially from list
    mainBin = Queue()
    for num in numList:
        mainBin.enqueue(num)

    #list of digit bins index 0 to 9
    digBin = []
    for digit in range(0,10):
        digBin.append(Queue())

    #max decimal int place
    maxPlace = 0

    #list of digits as strings
    numListStr = []
    for i in range(len(numList)):
        numListStr.append(str(numList[i]))
    for strng in numListStr:
        if len(strng) > maxPlace:
            maxPlace = len(strng)
    print('Max 10s place is: ' + str(10**(maxPlace-1)))
    
    #need way to get 1s, 10s, 100s... add to bin queues
    for placeIdx in range(0, maxPlace):
        place = 10**placeIdx
        print('Current place is: ' + str(place))
        #get the single digit of the place, put in digBin
        while not mainBin.isEmpty():
            num = mainBin.dequeue()
            if num < place:
                digBin[0].enqueue(num)
            else:
                x = placeIdx
                numPlace = 0
                while x != 0:
                    numPlace = num//10
                    x = x - 1
                digit = numPlace % 10
                digBin[digit].enqueue(num)
        #all numbers in bins now, collect back to main bin
        for i in range(10):
            while not digBin[i].isEmpty():
                mainBin.enqueue(digBin[i].dequeue())
                         
    #return a list of sorted numbers
    sortedList = []
    while not mainBin.isEmpty():
        sortedList.append(mainBin.dequeue())
    return sortedList

def main():
    listt = [667, 534, 1234, 69, 4]
    print('List to be sorted with radix: ')
    print(listt)
    print('Result: ')
    print(radixSort(listt))

main()
