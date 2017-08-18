#!usr/bin/python3

'''
Q2.4
    Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. lf x is contained within the list, the values of x only need to be after the elements less than x (see below).The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.
94

EXAMPLE
Input: 3 -> 5 -> 8 -> 5 ->10 -> 2 -> 1[partition=5) 
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
'''

from LinkedList import LinkedList
from LinkedList import LLNode

#O(n) time, O(n) space
def partition_w_list(ll, x):
    if ll.head is None:
        return
    curr = ll.head
    lst = []
    while(curr):
        lst.append(curr.value)
        curr = curr.next

    curr = ll.head #refresh curr to head
    lst = sorted(lst) #sort list

    for i in lst:
        curr.value = i
        curr = curr.next
    
#O(n^2) time  & O(1) space
def partition_w_runner(ll, x):
    if ll.head is None:
        return
    curr = ll.head

    while(curr):
        if curr.next:
            runner = curr.next
        else:
            return
        if curr.value >= x:
            swapped = False
            while(runner):
                if runner.value < x:
                    curr.value, runner.value = runner.value, curr.value
                    swapped = True
                    break
                else:
                    runner = runner.next
            if not swapped:
                return
        curr = curr.next

#O(n) time, O(n) space
def partition_w_two_ll(ll, x):
    if ll.head is None:
        return

    lessLL = LinkedList()
    greaterEqLL = LinkedList()

    for curr in ll:
        if curr.value < x:
            lessLL.push(curr.value)
        else:
            greaterEqLL.push(curr.value)

    if lessLL.is_empty():
        return greaterEqLL
    elif greaterEqLL.is_empty():
        return lessLL
    else:
        lessLL.tail.next = greaterEqLL.head
        greaterEqLL.head = None
        ll.head = lessLL.head
        lessLL.head = None

#O(n) time, O(1) space
def partition_inplace(ll, x):
    if ll.head is None:
        return
   
    start = False #if there are elements less than v
    end = ll.tail
    curr = ll.head
     
    while( curr is not end.next ):
        if curr.value < x:
            ll.shift(curr.value)
            if not start:
                start = ll.head
        else:
            ll.push(curr.value)
        curr = curr.next

    if start:
        start.next = end.next
    else:
        ll.head = end.next


def partition(ll, x):
    current = ll.tail = ll.head
    
    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None

ll = LinkedList()
ll.generate(3, 0, 99)
print(ll)
partition(ll, ll.head.value)
#partition_w_list(ll, ll.head.value)
#partition_w_runner(ll, ll.head.value)
#partition_w_two_ll(ll, ll.head.value)
#partition_inplace(ll, ll.head.value)
print(ll)
