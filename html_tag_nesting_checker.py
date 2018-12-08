#this checks HTML document for properly nested
#open and closing tags: <html>xxxxx</html>

from pythonds.basic.stack import Stack
import os

def htmlCheck(htmlFileDirStr):
    fileObj = open(htmlFileDirStr)
    content = fileObj.read()
    fileObj.close()
    
    tagStack = Stack()
    
    tagList = []
    for charIdx in range(len(content)):
        tempStr = ""
        if content[charIdx] == "<":
            tempIdx = charIdx
            while content[tempIdx] != ">":
                tempStr = tempStr + content[tempIdx]
                tempIdx += 1
            tagList.append(tempStr)
    print(tagList) #debug helper

    #meat and potatoes: the stack logic
    for i in range(len(tagList)):
        if "</" in tagList[i]: #closing marker
            if tagStack.peek()[1:] in tagList[i]:
                #debug print statement
                print("observed tag from list is: %s, about to pop \
from stack: %s" % (tagList[i], tagStack.peek()))
                tagStack.pop()
            else:
                return False
        elif "<" in tagList[i]:
            #debug print statement
            print("about to push to stack: %s" % tagList[i])
            tagStack.push(tagList[i])

    if tagStack.isEmpty():
        return True
    else:
        return False

#main 
unformattedPath = r"C:\Users\Eric\Desktop\python_learn\html_example_txt\html_example.txt"
pathFilesSplit = unformattedPath.split("\\")
htmlPath = os.getcwd()
for i in range(-2, 0, 1):
    htmlPath = os.path.join(htmlPath, pathFilesSplit[i])                                       
                                       
print("The file is html legal: %s" % htmlCheck(htmlPath))

##C:\Users\Eric\Desktop\python_learn\html_example_txt\html_example.txt
##
##<html>
##   <head>
##      <title>
##         Example
##      </title>
##   </head>
##
##   <body>
##      <h1>Hello, world</h1>
##   </body>
##</html>
