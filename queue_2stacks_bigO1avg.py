#implement a queue so both en/de-queue have avg O(1)

#answer is this is can be done with 2 stacks:

from pythonds.basic.stack import Stack

class Queue2Stacks:
    def __init__(self):
        self.stackIn = Stack()
        self.stackOut = Stack()

    def enqueue(self, item):
        self.stackIn.push(item)

    def dequeue(self):
        if self.stackOut.isEmpty():
            while not self.stackIn.isEmpty():
                self.stackOut.push(self.stackIn.pop())
            return self.stackOut.pop()
        else:
            return self.stackOut.pop()

    def isEmpty(self):
        ##bug FIXED: Returns True when should be False
        return self.stackIn.isEmpty() and \
               self.stackOut.isEmpty()
        #debug prints
        print("stackIn empty?: %s" % self.stackIn.isEmpty())
        print("stackOut empty?: %s" % self.stackOut.isEmpty())

    def size(self):
        size = self.stackIn.size() + self.stackOut.size()
        return size

q = Queue2Stacks()

print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())	 
q.enqueue(8.4)	 
print(q.dequeue())	 
print(q.dequeue())	 
print(q.size())
