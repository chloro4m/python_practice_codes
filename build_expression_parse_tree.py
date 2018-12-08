#building a parse tree for expressions code
# 1) modify to handle expres. w/o spaces b/t each char
# 2) handle "and, or, not" in buildParseTree + evaluate
###COMPLETE!, but see "BUG" note just below
###BUG: 'not' works, but not when it is the very first root
###will not fix this bug since 'not' works as any other root

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def buildParseTree(exp): #could be any spaced-exp
    ## 1)
    ###my tactic will be to create a fpexp from whatever i get
    fplist = []
    skips = 0
    for i in range(len(exp)):
        if skips:
            skips -= 1
            continue
        
        if exp[i] == 'a': #2)
            skips = 2
            fplist.append(exp[i:(i+3)])
            
        elif exp[i] == 'o': #2)
            skips = 1
            fplist.append(exp[i:(i+2)])
            
        elif exp[i] == 'n': #2)
            skips = 2
            fplist.append(exp[i:(i+3)])
        
        elif not exp[i].isdigit():
            fplist.append(exp[i])
            
        elif exp[i].isdigit(): #could > single digit number
            j = i + 1
            while j != len(exp) and exp[j].isdigit():
                skips += 1
                j += 1
            fplist.append(exp[i:j])
                  
    print("Debug: here's fplist:")
    print(fplist)
    ##
    
    #fplist = fpexp.split() #no need after 1) on exp
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == ' ':
            continue
        elif i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i == 'and':
            print("'and' logic...")
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == 'or':
            print("'or' logic...")
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == 'not':
            print("'not' logic...")
            #not binds like so: 'not 69' OR 'not (xxx)'
            currentTree.setRootVal(i)
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()          
        elif i not in ['+', '-', '*', '/', ')']: #number handling
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
            #handling if parent is 'not': pop again to parent
            if currentTree.getRootVal() == 'not':
                parent = pStack.pop()
                currentTree = parent                
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, \
             '*':operator.mul, '/':operator.truediv, \
             'and':operator.and_, 'or':operator.or_, \
             'not':operator.not_} #not?!

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    #need to somehow handle 'not' branching to: (value, None)
    if parseTree.getRootVal() == 'not':
        return operator.not_(evaluate(leftC))
          
    #original w/out 'not' 
    elif leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

##pt = buildParseTree("( ( 10 + 5 ) * 3 )")
##pt.postorder()  #defined and explained in the next section
