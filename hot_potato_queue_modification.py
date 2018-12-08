##Modify the Hot Potato simulation to allow for a
##randomly chosen counting value so that each pass
##is not predictable from the previous one

from pythonds.basic.queue import Queue
import random

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(random.randrange(0,num)):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

for i in range(10):
    print(hotPotato(["Bill","David","Susan","Jane",\
                 "Kent","Brad"],7))
