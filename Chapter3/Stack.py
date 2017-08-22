#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def peek(self): #return but do not remove top element
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self.data.pop()

