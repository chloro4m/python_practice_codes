#make a basic perfect hash function
#use a list of 11 names, tablesize = 11

import random

##def plainHash(astring, tablesize):
##    sum = 0
##    for pos in range(len(astring)):
##        sum = sum + ord(astring[pos])
##    return sum%tablesize

##print("Regular charSum hash values: ")
##for string in nameList:
##    print(string," %d"%plainHash(string, 11))

#Cichelli's method:
#h(S) = S.length() + g(S[0]) + g(S[S.length()-1])

def CichelliHash(strList):
    #can make minPerfectHash w/ small lists
    tblSize = len(strList)
    
    #find frequency of each first and last letter
    outerCharFreq = {}
    gVal = {}
    for name in nameList:
        if name[0] not in outerCharFreq:
            outerCharFreq[name[0]] = 1
            gVal[name[0]] = None
        else:
            outerCharFreq[name[0]] += 1
        if name[-1] not in outerCharFreq:
            outerCharFreq[name[-1]] = 1
            gVal[name[-1]] = None
        else:
            outerCharFreq[name[-1]] += 1
    #print("gVal: %s\n"%gVal)#DEBUG    
    #score words by sum of first/last letter freq
    outerCharsScore = {}
    for name in nameList:
        outerCharsScore[name] = outerCharFreq[name[0]] +\
                                outerCharFreq[name[-1]]
                                
    #sort in that order. dict={name:score...}
    words = [(k, v) for k, v, in outerCharsScore.items()]
    wordsSorted = sorted(words, key=lambda x:x[1], reverse = True)                                                                                   
    #print("Below are ready for g(outerChar) selection:\n")
    #print(wordsSorted) #all code correct up to here so far
    wordList = []
    for wordVal in wordsSorted: #word is tuple ('name',score)
        wordList.append(wordVal[0])
    print("This is the wordlist: %s"%wordList)#DEBUG

    #for each word in order, choose g(x) for each possible
    #first/last letter so each word gets unique h(S) value
    edgeChars = [] #tuples of edge chars per word in wordList
    for w in range(len(wordList)):
        edgeChars.append(wordList[w][0] + wordList[w][-1])
    #print("edgeChars: %s\n"%edgeChars)
    hashTbl = [None] * tblSize
    res = None
    for word in wordList:
        print("\nWorking on this word: %s"%word)#DEBUG
        firstChar = word[0]
        lastChar = word[-1]
        if gVal[firstChar] == None: #give the char a gVal if none assigned yet    
            gVal[firstChar] = 0
        if gVal[lastChar] == None: #same with last char
            gVal[lastChar] = 0
        res = computeH(word, gVal[firstChar], gVal[lastChar], tblSize)
        if hashTbl[res] == None:
            hashTbl[res] = word
            print("Sucessfully hashed.")
        else:
            print("Hash collision detected.")
            #need to change gValues until empty hash slot can be filled
            #determine if we are in case#1(easy) or case#2(hard)
            case_easy = False
            case_hard = False
            first = 0
            last = 0
            stopIdx = wordList.index(word)
            for i in range(stopIdx):
                if firstChar in edgeChars[i]:
                    first += 1
                if lastChar in edgeChars[i]:
                    last += 1
            targetChar = ""
            if first == 0:
                    targetChar = firstChar
                    case_easy = True
            elif last == 0:
                    targetChar = lastChar
                    case_easy = True
            else:
                    case_hard = True
            print("Case easy: %s, Case hard: %s. TargetChar: %s"%(case_easy, case_hard, targetChar))
            #case 1: one of the edge chars hasnt been seen yet        
            if case_easy == True:
                loop = True
                while loop == True:
                    gVal[targetChar] += 1 #increment gVal
                    res = computeH(word, gVal[firstChar], gVal[lastChar], tblSize)
                    if hashTbl[res] == None:
                        hashTbl[res] = word
                        print("Easy collision resolved.")
                        loop = False
                    else:
                        continue
            
            #case 2: both edge chars seen already
                    #USING CHAINING TO CHEAT THRU THIS!!!
            if case_hard == True:
                print("Tough spot, need to recompute backwards.")
                print("Cheating and deciding to chain the value to the hash collision spot instead.")
                tblSlotChain = []
                tblSlotChain.append(hashTbl[res])
                tblSlotChain.append(word)
                hashTbl[res] = tblSlotChain

##                #update one gVal[edgeChar] until all valid hash slots used
##                
##                #arbitrary choice of firstChar to recompute with
##                targetChar = firstChar
##                #set the to-be-affected hash slots back to None
##                #?
##                #perform looped logic
##                loop = True
##                while loop == True:
##                    #completely resetting hash table
##                    hashTbl = [None] * tblSize
##                    print(hashTbl)
##                    gVal[targetChar] += 1
##                    #recompute H for all entries with target, up to
##                    #and including stopIdx/curWord
##                    for w in range(stopIdx+1): #includes problem word
##                        newH = computeH(wordList[w], gVal[firstChar], gVal[lastChar], tblSize)
##                        #check validity of new hash value
##                        if hashTbl[newH] == None:
##                            hashTbl[newH] = wordList[w]
##                            print("New temp hard hash OK")
##                            loop = False 
##                        else: #no good, keep incrementing gVal in new loop
##        
##                            print("New temp hard hash not OK, should re-loop and gVal[target]++")
##                            print("The bad newH is %s, the hashTbl is %s"%(newH, hashTbl))
##                            loop = True
##                            break
##                    continue
                                    
    print("\nHere's the final MinPerfectHash:")
    print(hashTbl)
    print("\nAnd here's the g-value mappings: ")
    print(gVal)
    print("\nedgeChars: %s"%edgeChars)

#wordlist: ['lean', 'michael', 'jean', 'leo', 'jake', 'joshua', \
    #'crystal', 'finn', 'mike', 'alex', 'terry']

def computeH(string, gValFirst, gValLast, tablesize):
    h = len(string) + gValFirst + gValLast
    return h % tablesize

#main call
nameList=["alex", "leo", "terry", "jake", "finn", "mike", "lean", "michael", "joshua", "crystal", "jean"]
CichelliHash(nameList)                                        
