#Write a function revstring(mystr)
#that uses a stack to reverse the characters in a string.

class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        popped = self.s[ len(self.s)-1 ]
        del self.s[ len(self.s)-1 ]
        return popped
        #can also just use: return self.items.pop()
        
    def peek(self):
        return self.s[ len(self.s)-1 ]

    def isEmpty(self):
        return self.s == []
    
    def size(self):
        return len(self.s)
        

def revStrStk(string):
    #pop items from string stack and push them in order
    #into new stack
    s = Stack()
    for i in range(len(string)):
        s.push(string[i])
    revStr = ''
    while not s.isEmpty():
        revStr += s.pop()
    print(revStr)
        
    #need to set a new string that is reversed and print it

def main():
    string = 'helloWorld'
    print('String to reverse is %s.' % string)
    print('Here is it reversed w/ stack implementation: ')
    revStrStk(string)

main()
