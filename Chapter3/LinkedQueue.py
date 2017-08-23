#!/usr/bin/python3

class LinkedQueue():
    #FIFO 
    #front/first ------> back/last
    #head -> 1 -> 2 -> 3 -> tail
    #pop at head, push at tail
    class Node():
        def __init__(self, data, nextNode):
            self.data = data
            self.next = nextNode
    
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        if self.is_empty():
            self.head = self.tail = self.Node(data, None)
        else:
            self.tail.next = self.Node(data, None)
            self.tail = self.tail.next
        self.size += 1

    def peek(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.head.data

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        e = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        return e

#------------TEST-------------
def test(queue):
    node = queue.head
    lst = []
    print("head: ", end="")
    while node:
        lst.append(str(node.data))
        node = node.next
    print( "->".join(lst), end="")
    print(" :tail")
    
queue = LinkedQueue()
for i in range(5):
    queue.enqueue(i)
    test(queue)
for i in range(5):
    print("Peek:", queue.peek())
    queue.dequeue()
    test(queue)

