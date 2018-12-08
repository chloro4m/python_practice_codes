#water gallon jugs problem

#4gal and 3gal, make 2gal in 4gal

#generalize: yGal, xGal, zGal in yGal where y>x
#vol_2 > vol_1

def galJugs(vol_1, vol_2, jug_1, jug_2, endVolume):
    
    if vol_1 >= vol_2:
            raise Exception("vol_2 must be bigger than vol_1!")
        
    while 1:
        if len(jug_2) == endVolume:
                print("Answer found [outer While loop]!")
                break
        fill(jug_2, vol_2)
        print("jug_2: %d, jug_1: %d"%(len(jug_2), len(jug_1)))
        while len(jug_2) > 0:
            dumpIn(jug_2, jug_1, vol_1)
            print("jug_2: %d, jug_1: %d"%(len(jug_2), len(jug_1)))
            if len(jug_2) == endVolume:
                print("Answer found!")
                break
            if len(jug_2) == 0:
                break
            else:
                empty(jug_1)
                print("jug_2: %d, jug_1: %d"%(len(jug_2), len(jug_1)))
            
    return
    
def fill(jug, jug_max):
    while len(jug) < jug_max:
        jug.append(1)

def dumpIn(fromJug, toJug, toJugMax): 
    while len(fromJug) > 0 and len(toJug) < toJugMax:
        toJug.append(fromJug.pop())

def empty(jug):
    while len(jug) != 0:
        jug.pop()

       
##jug1 = []
##jug2 = []
##galJugs(3, 4, jug1, jug2, 2)

##j11 = []
##j4 = []
##galJugs(4, 11, j4, j11, 1)

j3 = []
j5 = []
galJugs(3, 5, j3, j5, 4)
