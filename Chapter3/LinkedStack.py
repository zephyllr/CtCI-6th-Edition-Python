#!/usr/bin/python3

#Stack implementation using singly linked list

class LinkedStack():
    #LIFO
    #top/last ------------> base
    #head -> 3 -> 2 -> 1 -> None
    #pop at head, push at head
    class Node():
        def __init__(self, data, nextNode):
            self.data = data
            self.next = nextNode

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None #top of stack
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, data):
        self.head = self.Node(data, self.head)
        self.size += 1

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.head.data

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        e = self.head.data
        self.head = self.head.next #bypass former top node
        self.size -= 1
        return e

