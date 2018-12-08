#binary tree with lists of lists

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root,newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch, [], []])
    return root

def insertRight(root,newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

#practice code to build this tree:
#   a
#b   c
# d  ef

tree = BinaryTree('a')
insertLeft(tree, 'b')
insertRight(tree, 'c')
insertRight(getLeftChild(tree), 'd')
insertLeft(getRightChild(tree), 'e')
insertRight(getRightChild(tree), 'f')

print('Here\'s the bin tree a->(L)b&(R)c b->(R)d c->(L)e&(R)f')
print(tree)
