#parse tree to calculate:
#derivative w.r.t. some variable
#THIS CODE IS ONLY PARTIAL TO HANDLE EASY CASES!!!
#Very hacky solution that isnt useful.

from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()

        elif i == ')':
            currentTree = pStack.pop()

        elif i.isalpha():
            currentTree.setRootVal(i)
            parent = pStack.pop()
            currentTree = parent

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

##def evaluate(parseTree):
##    opers = {'+':operator.add, '-':operator.sub, \
##             '*':operator.mul, '/':operator.truediv}
##
##    leftC = parseTree.getLeftChild()
##    rightC = parseTree.getRightChild()
##
##    if leftC and rightC:
##        fn = opers[parseTree.getRootVal()]
##        return fn(evaluate(leftC),evaluate(rightC))
##    else:
##        return parseTree.getRootVal()

def evalD(parseTree):
    res = ''
    res = evalDyDx(parseTree)
    return res[1:]

def evalDyDx(parseTree):
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()
    
    if leftC and rightC:
        root = parseTree.getRootVal()
        if root == '*':
            return multDyDx(evalDyDx(leftC), evalDyDx(rightC))
        elif root == '/':
            return divDyDx(evalDyDx(leftC), evalDyDx(rightC))
        elif root == '+':
            return addDyDx(evalDyDx(leftC), evalDyDx(rightC))            
        elif root == '-':
            return subDyDx(evalDyDx(leftC), evalDyDx(rightC))
    else: #base case, if leaf
        return parseTree.getRootVal()
        
def multDyDx(left, right):
##    print(leftVal)
##    left = leftVal.getRootVal() #bug?
##    right = rightVal.getRootVal()
    if left == 'x':
        res = 'D' + str(right)
        return res
    elif right == 'x':
        res = 'D' + str(left)
        return res
    else:
        return 0

def divDyDx(left, right):
##    left = leftVal.getRootVal()
##    right = rightVal.getRootVal()
    if left == 'x': 
        res = 'D' + '1/' + str(right)
        return res
    elif right == 'x':
        res = 'D' + '-' + str(left) + 'x^-2'
        return res

def addDyDx(left, right):
##    left = leftVal.getRootVal()
##    right = rightVal.getRootVal()
    
    leftStr = str(left)
    rightStr = str(right)
    if leftStr[0] == 'D':
        return leftStr
    elif rightStr[0] == 'D':
        return rightStr
    else:    
        if left == 'x' or right == 'x':
            res = 'D' + str(1)
            return res
        else:
            return 0
    
def subDyDx(leftl, right):
##    left = leftVal.getRootVal()
##    right = rightVal.getRootVal()
    if left == 'x': # 'x - num'
        res = 'D' + str(1)
        return res
    elif right == 'x': # 'num - x' 
        res = 'D' + str(-1)
        return res
    else:
        return 0    

pt = buildParseTree("( 9 + ( 6 * x ) )")
pt.inorder()
res = evalD(pt)
print("Derivative is %s\n"%res)

pt2 = buildParseTree("( ( 6 / x ) + 9 )")
pt2.inorder()
res2 = evalD(pt2)
print("Derivative is %s\n"%res2)

pt3 = buildParseTree("( ( x / 6 ) + 9 )")
pt3.inorder()
res3 = evalD(pt3)
print("Derivative is %s\n"%res3)


