#!/usr/bin/python3

'''
Q2.8
    Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop.

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to make a loop in the linked list.

EXAMPLE
Input: A -> B -> C -> D -> E -> C [the same C as earlier]
Output: C 
'''

from LinkedList import LinkedList

#O(n) time, O(n) space
def loop_detection_set(ll):
    curr = ll.head
    nodes = set()
    while curr: 
        if curr in nodes:
            return curr.value
        else:
            nodes.add(curr)
        curr = curr.next
    return False

#O(n) time, O(n) space
def loop_detection_runner(ll):
    slower = faster = ll.head
    while faster and faster.next and faster is not slower:
        slower, faster = slower.next, faster.next.next
    
    if fast is None or fast.next is None:
        return None

    slower = ll.head
    while faster is not slower:
        slower, faster = slower.next, faster.next

    return faster

