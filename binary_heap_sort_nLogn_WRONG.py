##Using the buildHeap method, write a sorting function
##that can sort a list in O(nlogn) time
##MAJOR BUGS in this implementaion :(

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

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

    #this builds heap in O(n) time
    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
	
    # 8)
    def binHeapSort(self, heap_list, start, end): #call with slices
        #the top level(0) single node needs slotting in
        print("\nStart idx: %s. End idx: %s"%(start, end))
        print("self.heapList: ")
        print(self.heapList)
        print("Passed in heap_list:")
        print(heap_list)
        self.heapList[start] = heap_list[1]
        #base case:        
        if end - start == 1:
            print("Base case:")
            temp = BinHeap()
            #temp.buildHeap(heap_list[start:end+1]) #bug?
            temp.buildHeap(heap_list[1:]) #bug fix?
            print("self.heapList: ")
            print(self.heapList)
            print("temp.heapList: ")
            print(temp.heapList)
            self.heapList[start] = temp.heapList[1]
            self.heapList[end] = temp.heapList[2]
            return
        
        else:
            level = 1
            while ((2**level)*2) < len(heap_list):
                a = 2**level #idx of first node in row
                b = a + a - 1 #row last idx
                temp = BinHeap()
                temp.buildHeap(heap_list[a:b+1])
                self.binHeapSort(temp.heapList, a, b)
                level += 1
            #need something for stragglers at the end?
            a = 2**level #here, 'a' is first node of last level
            #if last level has just one node:
            if a == len(heap_list)-1:
                self.heapList[end] = heap_list[-1]
            #if last level has >1 node:
            elif a < len(heap_list)-1:
                temp = BinHeap()
                temp.buildHeap(heap_list[a:len(heap_list)-1])
                self.binHeapSort(temp.heapList, start, end) #start/end arguments?
            else: #no nodes
                return
                
b=BinHeap()
x = [27, 17, 33, 21, 19, 18, 14, 11, 9, 5]
#x = [3, 1, 12, 2]
b.buildHeap(x)
print("Initial heap: ")
print(b.heapList)
b.binHeapSort(b.heapList, 1, b.currentSize)
print("Heap sorted result:")
print(b.heapList)


