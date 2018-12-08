#implement dequeue (double-end) w/ linked lists

##Deque() creates a new deque that is empty. It needs no parameters and returns an empty deque.
##addFront(item) adds a new item to the front of the deque. It needs the item and returns nothing.
##addRear(item) adds a new item to the rear of the deque. It needs the item and returns nothing.
##removeFront() removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
##removeRear() removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
##isEmpty() tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
##size() returns the number of items in the deque. It needs no parameters and returns an integer.

class DequeLL:
    def __init__(self):
        self.deque = UnorderedList()

    def isEmpty(self):
        return self.deque.size() == 0

    def addFront(self, item): #ill call the head the "front"
        self.deque.add(item)

    def addRear(self, item): #"rear" is the end of list
        self.deque.append(item)

    def removeFront(self):
        temp = self.deque.head
        self.deque.head = self.deque.head.getNext()
        return temp

    def removeRear(self):
        return self.deque.pop()

    def size(self):
        return self.deque.size()

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.lenList = 1 #13.

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item): #15. no handling of dupes needed
        temp = Node(item)
        temp.setNext(self.head)
        if self.head != None: #13. fixed bug: when list is empty
            temp.lenList += self.head.lenList 
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None: #14
                print("Item not in list! List unmodified.")
                return
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            current.getNext().lenList = self.head.lenList - 1 #13
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            self.head.lenList -= 1 #13

    def __str__(self): #17 bugs in output...fixed.
        res = []
        current = self.head
        if current == None:
            print("No items in list.")
        res.append(current.getData())
        current = current.getNext()
        while current != None:
            res.append(current.getData())
            current = current.getNext()
        return str(res)
            
#13. Implement "length" method to store in head instead
            #see Node class, need to update add+remove
    def length(self):
        return self.head.lenList

#18. Implement the remaining operations defined in the
#    UnorderedList ADT (append, index, pop, insert).

    def append(self, item):
        newNode = Node(item)
        current = self.head
        if current == None:
            self.head = newNode
        else:
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)
        #add to the node count
            self.head.lenList += 1

    def index(self, item):
        current = self.head
        if current == None:
            print("This list is empty.")
            return None
        else:
            index = 0
            while current != None:
                if current.getData() == item:
                    return index
                else:
                    current = current.getNext()
                    index += 1
            #only executes if item not there
            print("Item not in list.")
            return None
                
    def pop(self):
        previous = None
        current = self.head
        if current == None:
            print("List empty! Nothing to pop.")
            return None
        if self.size() == 1:
            temp = self.head
            self.head = None
            return temp
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        
        previous.setNext(None)
        return current
            
    def insert(self, pos, item):
        #error check
        if pos > self.size():
            raise Exception("Invalid index specified. Out of range.")
        newNode = Node(item)
        #logic for if pos=0, or head
        if pos == 0:
            newNode.setNext(self.head)
            self.head = newNode
            #add 1 to list counter
            self.head.lenList += 1
            return
        #go to index:pos->"current", also save pos-1 to "previous"
        current = self.head
        previous = None
        count = 0
        while count < pos:
            previous = current
            current = current.getNext()
            count += 1
        #have elem:(pos-1) point to newNode
        previous.setNext(newNode)
        #newNode points to elem
        newNode.setNext(current)
        #add 1 to list counter
        self.head.lenList += 1

#19

    def slice(self, start, stop):
        if start < 0 or stop > self.size():
            raise Exception("Slice bounds out of range.")
        if start >= stop:
            raise Exception("Start must be < Stop.")

        slice_ret = UnorderedList()
        
        begin = self.head
        idx = 0
        while idx < start:
            begin = begin.getNext()
            idx += 1

        slice_ret.head = begin #now we have [start:]
        
        end = slice_ret.head
        idx = 0
        while idx < (stop - 2):
            end = end.getNext()
            idx += 1

        #print("End value after logic: %d" % end.getData())
        end.setNext(None)

        #some logic to get length of slice...
        
        return slice_ret
