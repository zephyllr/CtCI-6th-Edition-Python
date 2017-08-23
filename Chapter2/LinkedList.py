#!/usr/bin/python3

#Main Linked List implementation for CtCi
from random import randint

class LLNode:

    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode #for doublyll

    def __str__(self):
        return str(self.value)

class LinkedList:
    
    def __init__(self, values=None):
        self.head = None #base of stack
        self.tail = None #for doublyll
        if values is not None:
            self.add_multiple(values)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __str__(self):
        values = [str(x) for x in self]
        return '-> '.join(values)

    def __len__(self):
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next
        return size 

    def is_empty(self):
        return self.head

    def push(self, value): #add to top/end/after tail
        if self.head is None:
            self.head = self.tail = LLNode(value)
        else:
            self.tail.next = LLNode(value)
            self.tail = self.tail.next
        return self.tail

    def shift(self, value): #add to base/beginning/before head
        if self.head is None:
            self.head = self.tail = LLNode(value)
        else:
            self.head = LLNode( value, self.head )
        return self.head
        
    def unshift(self): #remove from top/end/after tail
        if self.head is None:
            raise Empty('Linked List is empty')
        removed = self.head.value
        self.head = self.head.next
        return removed

    def add_multiple(self, values):
        #add multiple nodes
        for v in values:
            self.push(v)

    def generate(self, n, min_value, max_value):
        #generate random nodes
        self.head = self.tail = None
        for i in range(n):
            self.push(randint(min_value, max_value))
        return self

class DoublyLinkedList(LinkedList):

    def push(self, value):
        if self.head is None:
            self.head = self.tail = LLNode(value)
        else:
            self.tail.next = LLNode(value, None, self.tail)
            self.tail = self.tail.next
        return self
            
