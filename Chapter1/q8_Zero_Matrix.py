#!/usr/bin/python3

'''
Q1.8 
    Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
'''
import unittest

#O(N) space, O(NM) time
def zero_matrix(m):
    #store columns to change
    changeCol = set()
    #find 0's
    for row in range(len(m)):
        zeroRow = False
        for col in range(len(m)):
            if m[row][col] == 0:
                changeCol.add(col)
                zeroRow = True
        #zero out row with 0
        if zeroRow:
            m[row] = [0 for i in m[row]]
    #zero out columns with 0
    for col in changeCol:
        for row in range(len(m)):
            m[row][col] = 0
    #return new matrix
    return m

#---------------------------------------------------
#O(1) space, O(NM) time
def zero_matrix2(m):
    #use first row and col to check where to zero out 
    for row in range(1,len(m)):
        for col in range(1,len(m)):
            if m[row][col] == 0:
                m[0][col] = 0
                m[row][0] = 0
        #zero out row with 0
        if m[row][0] == 0:
            m[row] = [0 for i in m[row]]
    #zero out columns with 0
    firstRow = False
    for col in range(len(m[0])):
        if m[0][col] == 0:
            firstRow = True
            for row in range(len(m)):
                m[row][col] = 0
    #zero out first row if it contains 0
    if firstRow:
        m[0] = [0 for i in m[row]]

    return m

def print_matrix(matrix):
    for i in matrix:
        print(i)

#---------------------------------------------------
class Test(unittest.TestCase):
    #Test Cases
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 0, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 0, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 0, 0]
        ]),
        ([
            [1,2,0,3],
            [4,5,6,7]
        ], [
            [0,0,0,0],
            [4,5,0,7]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix2(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
