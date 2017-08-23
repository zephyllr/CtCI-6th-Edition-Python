#!/usr/bin/python3

'''
Q3.5
    Sort Stack: Write a program to sort a stack such that the smallest items are on the top/base. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array).The stack supports the following operations: push, pop, peek, and isEmpty.
'''

from Stack import Stack
import random

#O(n^2) time, O(n) space
def sort_stack(mainStack):
    tmpStack = Stack()
    tmpStack.push( mainStack.pop() ) #push first item
    while not mainStack.is_empty():
        tmpVar = mainStack.pop()
        while not tmpStack.is_empty() and tmpVar < tmpStack.peek():
            mainStack.push( tmpStack.pop() )
        tmpStack.push( tmpVar )
    return tmpStack 

def test(mainStack, tmpStack):
    print("mainStack:",mainStack)
    print("tmpStack:",tmpStack)

#--------TEST---------
mainStack = Stack()

for i in range(10):
    n = random.randint(1,20)
    mainStack.push(n)

print(mainStack)
mainStack = sort_stack(mainStack)
print(mainStack)

