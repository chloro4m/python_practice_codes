##Implement the Queue ADT, using a list such that the rear
##of the queue is at the end of the list.

import time

class QueueRearIsEnd:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class QueueFrontIsEnd:
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

##Design and implement an experiment to do benchmark
##comparisons of the two queue implementations. What
##can you learn from such an experiment?

#benchmark for front = end of list
start = time.time()
q1 = QueueFrontIsEnd()
for i in range(100000):
    q1.enqueue(i)
end = time.time()
print("Enqueue 100k ints takes this long with Front \
as end: %10.7f secs" % (end-start))

#benchmark for rear = end of list
start = time.time()
q2 = QueueRearIsEnd()
for i in range(100000):
    q2.enqueue(i)
end = time.time()
print("Enqueue 100k ints takes this long with Rear \
as end: %10.7f secs" % (end-start))

print("^Expected result: 2nd value should be way faster since Rear as end is simply an append to a list.")

