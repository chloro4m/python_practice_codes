#binary min heap that grows to only n items
#all lesser important items are dropped

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        self.maxSize = 10

    def setMaxHeapSize(self, size):
        self.maxSize = size

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      # 6)
      if self.currentSize == self.maxSize:
          currentMaxIdx = self.findMaxIdx()
          if self.heapList[currentMaxIdx] > k:
              #remove and replace the max
              self.replaceMax(currentMaxIdx, k)
          elif self.heapList[currentMaxIdx] == k:
              #do nothing, dont add
              print("Priority already in heap! No action.")
              return
          else:
              print("No action since this is lower priority than anything in the heap!")
      #the usual insert operation:
      else:
          self.heapList.append(k)
          self.currentSize = self.currentSize + 1
          self.percUp(self.currentSize)

    def maxChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if heapList[i*2] > heapList[i*2 + 1]:
                return i*2
            else:
                return i*2 + 1

    def isLeaf(self, i):
        if i * 2 > self.currentSize:
            return True
        else:
            return False
    
    def findMaxIdx(self): # 6)
        #the max will be one of the leafs
        idx = self.currentSize
        maxi = 0
        maxIdx = None
        while self.isLeaf(idx):
            if self.heapList[idx] > maxi:
                maxi = self.heapList[idx]
                maxIdx = idx
            idx -= 1
        return maxIdx

    def replaceMax(self, replaceIdx, newKey): # 6)
        self.heapList[replaceIdx] = newKey
        self.percUp(replaceIdx)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

##bh = BinHeap()
##bh.buildHeap([9,5,6,2,3])
##print(bh.delMin())
b=BinHeap()
x=[5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
b.buildHeap(x)
