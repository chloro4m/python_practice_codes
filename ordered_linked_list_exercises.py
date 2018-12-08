
##14. Implement "remove" so it works for when item not in list
##15. Allow list classes to have dupes. What methods impacted?
##17. Implement the __str__ method in the List class []
##20. Implement the remaining operations defined in the OrderedList ADT.

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self,item): #15 to allow dupes
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item): #14
        #if item is first in the list
        current = self.head
        if current.getData() == item:
            self.head = current.getNext()
            return
        #if item is somewhere inside the list
        previous = None
        while current != None:
            previous = current
            current = current.getNext()
            if current.getData() == item:
                previous.setNext(current.getNext())
                return

    def __str__(self): #17  
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

    #20: remaining methods
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

    def pop(self, pos):
        #if item is first in the list
        if pos == 0:
            current = self.head
            self.head = current.getNext()
            return current
        #if item is somewhere inside the list
        else:
            current = self.head
            previous = None
            count = 0
            while count < pos:
                count += 1
                previous = current
                current = current.getNext()
               
            previous.setNext(current.getNext())
            return current


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
