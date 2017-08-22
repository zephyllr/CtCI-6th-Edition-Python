#!/usr/bin/python3

'''
Q3.1 
    Three in One: Describe how you could use a single array to implement three stacks.
'''

class Multistack():
    def __init__(self, stacksize):
        self.numstacks = 3 #stacks 0,1,2
        self.data = [0] * (stacksize * self.numstacks)
        self.sizes = [0] * self.numstacks
        self.stacksize = stacksize

    #checks if specified stack is empty
    def is_empty(self, stacknum):
        return self.sizes[stacknum] == 0

    #checks if specified stack is full
    def is_full(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def getIndex(self, stacknum):
        return self.sizes[stacknum] + (stacknum)*self.stacksize

    #pushes element to specified stack
    def push(self, e, stacknum):
        if self.is_full(stacknum):
            raise Exception('Stack is full')
        self.data[ self.getIndex(stacknum) ] = e
        self.sizes[stacknum] += 1

    #peeks at top element of specified stack
    def peek(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        return self.data[ self.getIndex(stacknum)-1 ] 

    #pops top element of specified stack
    def pop(self, stacknum):
        if self.is_empty(stacknum):
            raise Exception('Stack is empty')
        popped = self.data[ self.getIndex(stacknum)-1 ]
        self.data[ self.getIndex(stacknum)-1 ] = 0
        self.sizes[stacknum] -= 1
        return popped

#-------------TEST----------------

def Three_in_One():
    stack = Multistack(3)
    test(stack)
    for stacknum in range(3):
        print(stack.is_empty(stacknum))
    for i in range(5,8):
        for stacknum in range(3):
            stack.push(i,stacknum)
            test(stack)
    for times in range(3):
        for stacknum in range(3):
            print(stack.is_full(stacknum))
            print(stack.peek(stacknum))
            print(stack.pop(stacknum))
            test(stack)

def test(stack):
    print(stack.data)
    print(stack.sizes)

Three_in_One()
