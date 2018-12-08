#find avg # comparisons for hash table for lambda vals
#cases: open address + linear probe VS. chaining
#subcases: success VS. unsuccess

def avgComp1(L): #open add. + lin. probe, success
    ans = 0.5 * (1 + 1/(1-L))
    return ans

def avgComp2(L): #open add. + lin. probe, fail
    ans = 0.5 * (1 + (1/(1-L))**2)
    return ans

def avgComp3(L): #chaining, success
    ans = 1 + (L/2)
    return ans

def avgComp4(L): #chaining, fail
    ans = L
    return ans

lambdaList = [.1, .25, .5, .75, .9, .99]

for L in lambdaList:
    print("For load factor = %f, avg # comparisons:"%L)
    a = avgComp1(L)
    b = avgComp2(L)
    c = avgComp3(L)
    d = avgComp4(L)
    print("for open add. + lin. probe, success: %f"%a)
    print("^^^, fail: %35f"%b)
    print("for chaining, success: %f"%c)
    print("^^^, fail: %20f\n"%d)

    
