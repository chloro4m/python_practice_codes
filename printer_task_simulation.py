##Self Check: DONE
##How would you modify the printer simulation to reflect a larger
##number of students? Suppose that the number of students was
##doubled. You make need to make some reasonable assumptions
##about how this simulation was put together but what would you
##change? Modify the code. Also suppose that the length of the
##average print task was cut in half. Change the code to reflect
##that change. Finally How would you parametertize the number of students,
##rather than changing the code we would like to make the
##number of students a parameter of the simulation.

from pythonds.basic.queue import Queue #need to download *ds !!!!

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

#added numStudents, should just affect max no. tasks
def simulation(numSeconds, pagesPerMinute, numStudents): 
#def simulation(numSeconds, pagesPerMinute): 

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask(numStudents):
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask(numStudents): #numStudents parameterized in here somehow
    secPerTask = 3600 / (2 * numStudents)  #<- need to fix bug with fraction division: DONE
    secPerTaskFloor = int(secPerTask)
    num = random.randrange(1,secPerTaskFloor+1) 
    if num == secPerTaskFloor:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5,10)
