#tower of hanoi w/ 3 stacks, use recursion too

from pythonds.basic.stack import Stack
#i think i'll use 3 lists as "stacks" so i can print

def moveTower(_from, to, spare, height):
    if height >= 1:
        moveTower(_from, spare, to, height-1)
        moveDisk(_from, to)
        moveTower(spare, to, _from, height-1)
    
    

def moveDisk(init, end):
    end.append(init.pop())


fromStack = [3, 2, 1]
toStack = []
spareStack = []


