#!/usr/bin/python3
'''
Q2.6 
    Palindrome: Implement a function to check if a linked list is a palindrome.
'''
from LinkedList import LinkedList

#O(n) time, O(n) space
def palindrome_reverse(ll):
    curr = ll.head
    rll = LinkedList()
    
    while curr:
        rll.shift(curr.value)
        curr = curr.next

    curr = ll.head
    rcurr = rll.head
    for i in range(len(ll)//2):
        if curr.value == rcurr.value:
            curr, rcurr = curr.next, rcurr.next
        else:
            return False
    return True

#O(n) time, O(1) space
def palindrome_expanded(ll):
    curr = start = ll.head
    
    while curr:
        ll.shift(curr.value)
        curr = curr.next

    curr = ll.head
    while start:
        if start.value == curr.value:
            start, curr = start.next, curr.next
        else:
            return False
    return True

#O(n) time, O(n) space
def palindrome_stack(ll):
    stack = []
    slow = fast = ll.head
    
    while fast:
        stack.append(slow.value)
        if not fast.next:
            break
        slow, fast = slow.next, fast.next.next

    while stack:
        if stack.pop() != slow.value:
            return False
        slow = slow.next
    return True

#TEST--------------------------------------------

ll = LinkedList()
values = list('racecar')
ll.add_multiple(values)
print(ll)
#print(palindrome_reverse(ll))
#print(palindrome_expanded(ll))
print(palindrome_stack(ll))

ll = LinkedList()
values = list('raccar')
ll.add_multiple(values)
print(ll)
#print(palindrome_reverse(ll))
#print(palindrome_expanded(ll))
print(palindrome_stack(ll))

ll = LinkedList()
values = list('educated')
ll.add_multiple(values)
print(ll)
#print(palindrome_reverse(ll))
#print(palindrome_expanded(ll))
print(palindrome_stack(ll))

