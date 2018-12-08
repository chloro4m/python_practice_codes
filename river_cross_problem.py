##Three missionaries and three cannibals come to a river
##and find a boat that holds two people. Everyone must get 
##across the river to continue on the journey. However, if
##the cannibals ever outnumber the missionaries on either
##bank, the missionaries will be eaten. Find a series of
##crossings that will get everyone safely to the other side
##of the river.

import random

def crossing(start, boat, end):
    if _QUIT == 1:
        print("Bad starting order here. Quitting.\n\n")
        return
    if len(end) == 6:
        print("Sucessfully crossed river!\n\n")
        return

    print("About to board boat.")
    onBoard(start, boat)
    printStatus(start, boat, end)

    print("About to off board person(s).")
    offBoard(end, boat)
    printStatus(start, boat, end)
    print("Returning to start.")
    
    crossing(start, boat, end) #recursive call

def onBoard(side, boat):
    while len(boat) < 2:
        while 1:
            temp = side.pop()
            if numPpl('C', side) > numPpl('M', side): #constraint
                side.insert(0, temp) #put back last in line
                continue
            boat.append(temp)
            break
    return
        
def offBoard(side, boat): 
    #if everyone is at the end + boat, drop off last 2 ppl
    if len(side) == 4:
        side.append(boat.pop())
        side.append(boat.pop())
        return
        
    #normal offBoarding logic #BUG: infinite loop???
    infinite_loop = 0
    while 1:
        if infinite_loop > 2:
            print("Infinite loop detected")
            global _QUIT
            _QUIT = 1
            return 
        temp = boat.pop()
        side.append(temp)
        #print("DEBUG: here's what non-final EndSide is:%s"%side)
        if (numPpl('C', side) > numPpl('M', side)) \
           and ('M' in side):
            boat.append(side.pop())
            infinite_loop += 1
            continue
        break
    return

def printStatus(start, boat, end):
    print("End is currently: %s"%end)
    print("Boat is currently: %s"%boat)
    print("Start is currently: %s\n"%start)
    return

def numPpl(M_or_C, listt):
    num = 0
    for person in listt:
        if person == M_or_C:
            num += 1
    return num

#main simulation below
#['M', 'C', 'M', 'C', 'M', 'C'] seems to yield winner

for i in range(3):
    #init. 3 lists to hold start, boat, end
    start = ['M', 'M', 'M', 'C', 'C', 'C']
    random.shuffle(start)
    print("Here's what we start with: %s"%start)
    
    boat = []
    end = []
    global _QUIT
    _QUIT = 0

    crossing(start, boat, end)
