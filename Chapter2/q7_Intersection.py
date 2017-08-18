#!/usr/bin/python3

'''
Q2.7
    Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
'''

from LinkedList import LinkedList

def intersection_stack(lla, llb):
    if lla.tail is not llb.tail:
        return False

    a, b = lla.head, llb.head
    stackA, stackB = [], []
    while a or b:
        if a:
            stackA.append(a)
            a = a.next
        if b:
            stackB.append(b)
            b = b.next
    
    intersect = False
    while stackA and stackB:
        popA, popB = stackA.pop(), stackB.pop()
        if popA is popB:
            intersect = popA.value
        else:
            return intersect

def intersection_inplace(lla, llb):
    if lla.tail is not llb.tail:
        return False
    #else an intersection exists
    diff = 0 
    print(len(lla), len(llb))
    if len(lla) > len(llb):
        diff = len(lla) - len(llb)
    elif len(lla) < len(llb):
        diff = len(llb) - len(lla)
        lla, llb = llb, lla
    longerN, shorterN = lla.head, llb.head

    for i in range(diff):
        longerN = longerN.next

    while longerN is not shorterN:
        longerN, shorterN = longerN.next, shorterN.next

    return longerN

def intersection_hash(lla, llb):
    if lla.tail is not llb.tail:
        return False
    hashA = set()
    
    nodeA, nodeB = lla.head, llb.head
    while nodeA:
        hashA.add(nodeA)
        nodeA = nodeA.next
    while nodeB:
        if nodeB in hashA:
            return nodeB
        nodeB = nodeB.next


#TEST
lla = LinkedList()
lla.add_multiple([1,2,3])
llb = LinkedList()
llb.add_multiple([0,1,2])
llb.tail.next = lla.tail
lla.add_multiple([4,5])
llb.tail = lla.tail
print(lla, llb)
llc = LinkedList()
llc.add_multiple([0,1,2,3,4,5])
#print(intersection_stack(lla, llb))
#print(intersection_inplace(lla, llb))
print(intersection_hash(lla, llb))
print(lla, llc)
#print(intersection_stack(lla, llc))
#print(intersection_inplace(lla, llc))
print(intersection_hash(lla, llc))

