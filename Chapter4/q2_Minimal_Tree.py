#!//usr//bin//python3

'''
Q4.2
    Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.
'''

class Node:
    def __init__(self, item):
        self.val = item
        self.right = None
        self.left = None

    def __str__(self):
        return '('+str(self.left)+':L ' + "V:" + str(self.val) + " R:" + str(self.right)+')'

def minimal_tree(lst):
    return create_min_tree(lst, 0, len(lst)-1)

def create_min_tree(lst, start, end):
    if start > end:
        return '' 
    mid = int((start + end)/2)
    midpt = Node(lst[mid])
    midpt.left = create_min_tree(lst, start, mid-1)
    midpt.right = create_min_tree(lst, mid+1, end)
    return midpt

#TEST----------------------------------------------------
lstA = [1,2,3]
lstB = [1,2,3,4,5,6,7]
lstC = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(minimal_tree(lstC))

