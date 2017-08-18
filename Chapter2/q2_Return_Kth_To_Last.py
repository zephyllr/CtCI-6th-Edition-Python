#!/usr/bin/python3

'''
Q2.2
    Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
'''

from LinkedList import LinkedList

#iterative algo
def kth_to_last_iter(ll, k):
    if ll.head is None:
        return
    curr = runner = ll.head

    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while(runner):
        curr = curr.next
        runner = runner.next

    return curr

#recursive algo - prints kth element
def kth_to_last_recA(head, k):
    if head is None:
        return 0
    i = kth_to_last_recA(head.next, k) + 1
    if i == k:
        print("Element:",i)
    return i

#recursive algo - returns kth element
def kth_to_last_recB(head, k):
    pass


#spacious and slow algo
def kth_to_last_with_size(ll, k):
    if ll.head is None:
        return
    curr = runner = ll.head
    size = 0

    while(runner.next):
        runner = runner.next
        size += 1
    
    for i in range(size - k + 1):
        curr = curr.next
    return curr.value


#TEST

ll = LinkedList()
ll.generate(10, 0, 99)
print("Original List")
print(ll)
print("Return 3rd to last")
print(kth_to_last_iter(ll, 3))
print(kth_to_last_recA(ll.head, 3))
print(kth_to_last_with_size(ll, 3))


