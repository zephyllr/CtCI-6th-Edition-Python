#!/usr/bin/python3

'''
Q3.3
    Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt(index) which performs a pop operation on a specific sub-stack.
'''

#The following version does not rollover elements from other stacks

class SetOfStacks():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
    
    class Stack():

        def __init__(self, capacity):
            self.capacity = capacity
            self.data = []

        def __len__(self):
            return len(self.data)

        def is_empty(self):
            return len(self.data) == 0

        def is_full(self):
            return len(self.data) == self.capacity

        def push(self, e):
            self.data.append(e)

        def peek(self):
            return self.data[-1]

        def pop(self):
            return self.data.pop()

        def __repr__(self):
            return str(self.data)

    def __len__(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stacks) == 0

    def push(self, e):
        if self.is_empty() or self.stacks[-1].is_full():
            self.stacks.append( self.Stack(self.capacity) )
        self.stacks[-1].push(e)

    def pop(self, index):
        if self.is_empty():
            raise Exception('Stack is empty')
        popped = self.stacks[index].pop()
        if self.stacks[index].is_empty():
            self.stacks.pop(index)
        return popped

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stacks[-1].peek()

    def __repr__(self):
        return str(self.stacks)

    
#--------------TEST-----------------

def Stack_of_Plates():
    multistacks = SetOfStacks(3)
    print(multistacks)
    for i in range(9):
        multistacks.push(i)
        print(multistacks)
    for i in range(2):
        for index in range(3):
            print(multistacks.peek())
            multistacks.pop(index)
            print(multistacks)
    
    for i in range(3):
        multistacks.push(i+10)
        #multistacks.pop(0)
        print(multistacks)
    
Stack_of_Plates()
