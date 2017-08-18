#!/usr/bin/python3

'''
Q2.3
    Delete Middle Node: Implement an algorithm to delete a node in the middle (Le., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.

EXAMPLE
    Input: the node c from the linked list a->b->c->d-e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e->f
'''

from LinkedList import LinkedList

def delete_middle_node(node):
    if node is None or node.next is None:
        return False
    node.value = node.next.value
    node.next = node.next.next

#TEST
ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.push(5)
print("Middle Node:", middle_node)
ll.add_multiple([7, 8, 9])

print("Original list")
print(ll)
print("Deleted middle node")
delete_middle_node(middle_node)
print(ll)
