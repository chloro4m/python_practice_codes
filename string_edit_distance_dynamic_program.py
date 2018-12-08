#4.15 NOT DONE!
#string edit distance problem, dynamic programming
##example: "algorithm" -> "alligator"
##-can copy letter for cost C=5
##-can delete letter for C=20
##-can insert for C=20
##-write dyn. prog. to minimize C b/t any 2 words

#first start with costs = 1 to make sure i have it right...

def costMin(fromWord, toWord, memo):
    #costs
    copyC = 1
    delC = 1
    insC = 1
    #levenshtein cost
##    copyC = 2
##    delC = 1
##    insC = 1

    m = len(fromWord)
    n = len(toWord)

    #init the distance to each char from the nullStr@idx=0
    for i in range(m+1):
        memo[(i, 0)] = i
    for j in range(n+1):
        memo[(0, j)] = j

    #start @(1,1) to fill boxes based on left, rt, diagDown boxes
    for j in range(1, n+1):
        for i in range(1, m+1):
            _ins = memo[(i, j-1)] + insC
            _del = memo[(i-1, j)] + delC
            if fromWord[i-1] == toWord[j-1]: #no cost if chars match
                _copy = memo[(i-1, j-1)] + 0
            else:
                _copy = memo[(i-1, j-1)] + copyC
                
            memo[(i, j)] = min(_ins, _del, _copy)

    print("The min-edit distance between",fromWord,"and",toWord,"is: ")
    print(memo[(m, n)])
#main part
#costMin('cab', 'bad')
cache={}
costMin('intention', 'execution', cache)
