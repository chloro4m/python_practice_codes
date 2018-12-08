#make binary max heap

#min heap code copy paste, will need to edit:

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i): #reverse polarities?? check
        while i // 2 > 0:
          if self.heapList[i] > self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i): #reverse polarities?? check
      while (i * 2) <= self.currentSize:
          mc = self.maxChild(i)
          if self.heapList[i] < self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def maxChild(self,i): #maxChild?? check
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] > self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMax(self): #delMax?? check, no change
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist): #reverse polarities?? check, no change
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

    def printHeap(self):
        level = 0
        node = 0
        breaker = False
        while True:
            if breaker:
                break
            else:
                rowCount = 2**level
                for i in range(rowCount):
                    node += 1
                    if node > self.currentSize:
                        breaker = True
                        break
                    else:
                        print(self.heapList[node], end=" ")
                print('\n')
                level += 1
        return
            
b = BinHeap()
x = [2, 4, 15, 223, 23, 5, 18, 3, 99]
b.buildHeap(x)
b.printHeap()
