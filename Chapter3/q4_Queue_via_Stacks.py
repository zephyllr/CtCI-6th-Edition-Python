#!/usr/bin/python3

'''
Q3.4
    Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
'''

from Stack import Stack

class Queue_w_2Stacks():
    def __init__(self):
        self.stackNew = Stack()
        self.stackOld = Stack()

    def old_is_empty(self): #return true if queue is empty
        return len(self.stackOld) == 0

    def new_is_empty(self): #return true if queue is empty
        return len(self.stackNew) == 0

    def add(self, item): #adds item to end of list, enqueue
        self.stackNew.push(item)

    def remove(self): #removes first item in list, dequeue
        if self.old_is_empty() and self.new_is_empty():
            raise Exception('Queue is empty')
        elif self.old_is_empty():
            self.new_to_old()
        return self.stackOld.pop()
    
    def peek(self): #returns top/first item of queue
        if self.old_is_empty() and self.new_is_empty():
            raise Exception('Queue is empty')
        elif self.old_is_empty():
            return self.stackNew.data[0]
        else:
            return self.stackOld.data[-1]
    
    def new_to_old(self):
        while not self.new_is_empty():
            self.stackOld.push( self.stackNew.pop() )

#----------------TEST---------------------
def queue_via_Stacks():
    queue = Queue_w_2Stacks()

    #add 5 items------------
    for i in range(5):
        print("Added:",i)
        queue.add(i)
        test(queue)
    print("Peeked:",queue.peek())

    #remove 3 items--------
    for i in range(3):
        print("Removed:",queue.remove())
        test(queue)

    #add 1 item------------
    print("Added:",5)
    queue.add(5)
    test(queue)

    #remove 1 item--------
    print("Removed:",3)
    queue.remove()
    test(queue)
    print("Peeked:",queue.peek())

def test(queue):
    print("New:",queue.stackNew)
    print("Old:",queue.stackOld)
    print("-------------------")

queue_via_Stacks()
