#!/usr/bin/python3 
'''
Q2.1 
    Remove Dups: Write code to remove duplicates from an unsorted linked list. 
    Follow Up: How would you solve this problem if a temporary buffer is not allowed?
'''

#set - hash with no keys
from LinkedList import LinkedList

def remove_dups(ll):
    if ll.head is None:
        return

    curr = ll.head
    uniqueSet = {curr.value} #or set([current.value]}

    while(curr.next):
        if curr.next.value in uniqueSet:
            curr.next = curr.next.next
        else:
            uniqueSet.add(curr.next.value)
            curr = curr.next
    return ll

def remove_dups_inplace(ll):

    if ll.head is None:
        return
        
    curr = ll.head
    while(curr):
        runner = curr
        while(runner.next):
            if runner.next.value == curr.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next

    return ll


#TEST
ll = LinkedList()
ll.generate(10, 0, 4)
print("Original LL")
print(ll)
remove_dups(ll)
print("Removed duplicates with ds")
print(ll)

ll.generate(10, 0, 4)
print("Original LL")
print(ll)
print("Removed duplicates inplace")
remove_dups_inplace(ll)
print(ll)

