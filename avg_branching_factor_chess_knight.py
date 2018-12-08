#chess board knight tour branching factor calculation
#(x,y)=(0,0) coord for board is lower left most unit

def chessKnightAvgBranchFactor(boardSize):
    if boardSize < 3:
        print("Error: The knight has nowhere to move!")
        return
    
    #storage for intermediate numbers?
    bFactors = []
    
    #set up 2 for loops to represent a coord for each square
    for y in range(boardSize):
        for x in range(boardSize):
            #for each square, get # legal moves
            unitRes = numLegalMoves(x, y, boardSize)
            #store legal moves value in list
            bFactors.append(unitRes)

    #when all values in list:
    #calculate avg and return value
    sum_ = 0
    for num in bFactors:
        sum_ += num
        
    return (sum_ / len(bFactors))

#legal non-overlapping moves:
# L|R|U|D
# 1|x|2|x.
# x|1|2|x.
# x|2|1|x.
# x|2|x|1.
# x|1|x|2.
# 1|x|x|2.
# 2|x|x|1.
# 2|x|1|x.
def numLegalMoves(xCoord, yCoord, boardSize):
    #list of the 8 scenarios
    #(x_offset, y_offset)
    offsets = ((-1,2), (1,2), (2,1), (2,-1), (1,-2), \
               (-1,-2), (-2,-1), (-2,1))
    #given each scenario, calculate new x and y
    valids = 0
    for offset in offsets:
        newCoord = (xCoord + offset[0], yCoord + offset[1])
        nc = newCoord
        #check if both x and y within boardSize-1
        if nc[0] < 0 or nc[0] > (boardSize-1) \
           or nc[1] < 0 or nc[1] > (boardSize-1):
            continue
        else: #legally on board after move
            valids +=1        
    #return the number of valid moves
    return valids

#unit tests:
    #size=2, error
    #size=3, k=?
    #size=5, k=3.8
    #size=6, k=4.4
    #size=8, k=5.25

def main():
    boardSizeList=[2, 3, 5, 6, 8]
    for size in boardSizeList:
        print("\nAvg branch factor for boardsize %d is:"%size)
        print(chessKnightAvgBranchFactor(size))

main()

