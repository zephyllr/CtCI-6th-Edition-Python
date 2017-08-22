#!/usr/bin/python3

class Queue():
    DEFAULT_CAPACITY = 10 #moderate capacity for all new queues

    def __init__(self): #create empty queue
        self.data = [None] * Queue.DEFAULT_CAPACITY
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size  == 0

    def enqueue(self, e):
        if is_empty():
            raise Empty('Queue is empty')
        if self.size == len(self.data):
            self.resize(2 * len(self.data))
        avail = (self.front + self.size) % len(self.data)
        self.data[avail] = e
        self.size += 1

    def dequeue():
        if is_empty():
            raise Empty('Queue is empty')
        front = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % len(self.data)
        self.size -= 1
        return front

    def peek(): #return but do not remove first element
        if is_empty():
            raise Empty('Queue is empty')
        return self.data[self.front]

    def resize(self, cap):
        old = self.data
        self.data = [None] * cap
        walk = self.front
        for k in range(self.size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self.front = 0 
