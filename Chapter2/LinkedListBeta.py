#!/usr/bin/python3

#Alice's Linked List Implementation 
class Node():
    def __init__(self, data=None, nextNode=None, prevNode=None):
        self.data = data
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.data)

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [ str(node) for node in self]
        return '->'.join(values)

    def __len__(self):
        node = self.head
        size = 0
        while node:
            size += 1
            node = node.next
        return size

    def is_empty(self):
        return self.head

    def add_to_end(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
        return self.tail

    def add_to_beginning(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, self.head)
        return self.head 

class DoublyLinkedList(LinkedList):
    def add_to_end(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.tail.next = Node(data, None, self.tail)
            self.tail = self.tail.next
    def add_to_beginning(self, data):
        if self.head is None:
            self.head = self.tail = Node(data)
            return self.head
        else:
            self.head = Node(data, self.head, None)
            self.head.next.prev = self.head
            return self.head
    def __str__(self):
        values = [ str(node) for node in self]
        return '<->'.join(values)


