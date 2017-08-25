#!/usr/bin/python3

class CircularQueue():
    #queue implmentation with circularly linked list
    # ...3->4->tail->head->1->2->...
    class Node():
        def __init__(self, data, nextNode):
            self._data = data
            self._next = nextNode

        def __str__(self):
            return str(self._data)
    
    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0

    def enqueue(self, data):
        if self.is_empty():
            self._tail = self.Node(data, None)
            self._tail._next = self._tail
        else:
            newNode = self.Node( data, self._tail._next )
            self._tail._next = newNode
            self._tail = newNode
        self._size += 1

    def peek(self): #element at front of queue
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._tail._next._data

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        oldHead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldHead._next
        self._size -= 1
        return oldHead._data

    def rotate(self): #rotate head element back to tail
        if self.is_empty():
            raise Exception('Queue is empty')
        self._tail = self._tail._next
  
    def __iter__(self):
        curr = self._tail
        for i in range(self._size):
            curr = curr._next
            yield curr
       
    def __str__(self):
        values = []
        for nodes in self:
            values.append(str(nodes._data))
        return '->'.join(values)

#TEST----------
def main():
    
    queue = CircularQueue()
    for i in range(5):
        queue.enqueue(i)
    print(queue)

    for i in range(5):
        queue.rotate()
        print(queue)

    for i in range(5):
        print('peeked:', queue.peek())
        print('dequeued:', queue.dequeue())
        print(queue)

main()
