#!/usr/bin/python3

'''
Q3.2
    Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''
import random

class Stack_with_Min():
    def __init__(self):
        self.data = []
        self.mins = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        if self.is_empty():
            self.mins.append(e)
            self.data.append(e)
        else:
            self.data.append(e)
            currMin = self.minv()
            if e < currMin:
                self.mins.append(e)

    def peek(self): #return but do not remove top element
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        popped = self.data.pop()
        if popped == self.minv():
            self.mins.pop()
        return popped

    def minv(self):
        return self.mins[-1]


#------------------TEST----------------------

def StackMin():
    stack = Stack_with_Min()
    test(stack)
    for i in range(7):
        rand = random.randint(1,20)
        stack.push(rand)
        test(stack)
    for i in range(7):
        print("min:",stack.minv())
        print(stack.pop())
        test(stack)

def test(stack):
    print(stack.data)
    print(stack.mins)

StackMin()    
