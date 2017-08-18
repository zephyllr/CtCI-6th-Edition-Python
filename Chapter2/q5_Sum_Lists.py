#!/usr/bin/python3

'''
Q2.5
    Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295. 
Output:2 -> 1 -> 9. That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem. 
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295. 
Output: 9 -> 1 -> 2. That is, 912.
'''

from LinkedList import LinkedList

#O(n) time
def sum_lists_reverse(lla, llb):
    currA = lla.head
    currB = llb.head

    while(currA or currB):
        #add 0 if numbers are not even in length
        if not currA:
            lla.push(0)
            currA = lla.tail
        elif not currB:
            llb.push(0)
            currB = llb.tail
        #add digits
        currA.value += currB.value
        #add one to next digits place if > 9
        if currA.value > 9:
            currA.value -= 10
            if currA.next:
                currA.next.value += 1
            else:
                lla.push(1)
        #continue to next digits
        currA, currB = currA.next, currB.next
    return lla

#O(n) time
def sum_lists_forward(lla, llb):
    if len(lla) > len(llb):
        diff = len(lla) - len(llb)
        for i in range(diff):
            llb.shift(0)
    elif len(lla) < len(llb):
        diff = len(llb) - len(lla)
        for i in range(diff):
            lla.shift(0)
    currA = lla.head
    currB = llb.head
    prevA = None

    while(currA or currB):
        currA.value += currB.value
        if currA.value > 9:
            currA.value -= 10
            if prevA:
                prevA.value += 1
            else:
                lla.shift(1)
        prevA = currA
        currA, currB = currA.next, currB.next

    return lla


def sum_lists(lla, llb):
    lstA, lstB = [], []
    for a in lla:
        lstA.append(a.value)
    for b in llb:
        lstB.append(b.value)
    
    numA = int("".join(map(str, lstA)))
    numB = int("".join(map(str, lstB)))
    sumForward = numA + numB

    lstA.reverse()
    lstB.reverse()
    numA = int("".join(map(str, lstA)))
    numB = int("".join(map(str, lstB)))
    sumReverse = numA + numB
    sumReverse = str(sumReverse)[::-1]
    
    return (sumForward, sumReverse)

#TEST
lla = LinkedList()
llb = LinkedList()
'''
#TEST - REVERSE
lla.generate(5, 9, 9)
llb.generate(3, 1, 9)
print("reverse lists")
print(lla)
print(llb)
print("reverse sum")
print(sum_lists(lla, llb)[1])
print(sum_lists_reverse(lla, llb))
'''
#TEST - FORWARD
lla.generate(5, 1, 9)
llb.generate(3, 1, 9)
print("forward lists")
print(lla)
print(llb)
print("forward sum")
print(sum_lists(lla, llb)[0])
print(sum_lists_forward(lla, llb))
