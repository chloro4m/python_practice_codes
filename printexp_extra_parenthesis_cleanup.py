##Clean up the printexp function so that it does
##not include an ‘extra’ set of parentheses around
##each number.

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

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return eTree

def printexp(tree):
  sVal = ""
  if tree:
  
      if type(tree.getRootVal()) == int:
            sVal = printexp(tree.getLeftChild())
      else:
          sVal = '(' + printexp(tree.getLeftChild()) #core

      sVal = sVal + str(tree.getRootVal()) #core

      if type(tree.getRootVal()) == int:
          sVal = sVal + printexp(tree.getRightChild())
      else:
          sVal = sVal + printexp(tree.getRightChild())+')' #core
          
  return sVal

def printexp2(tree):
  sVal = ""
  if tree:
      sVal = '(' + printexp2(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp2(tree.getRightChild())+')'
  return sVal

p = buildParseTree("( 10 + 5 )")
print(printexp(p))

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(printexp(pt))
#need to clean up this output: (((10)+(5))*(3))
