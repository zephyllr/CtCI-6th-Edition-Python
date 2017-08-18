#!/usr/bin/python3

"""
Question 1.7
    Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
"""

import unittest

def rotate_matrix(m):

    for i in range(len(m)//2):
        for j in range(i, len(m)-1-i):

            m[i][j], m[j][-1-i], m[-1-i][-1-j], m[-1-j][i] =\
            m[-1-j][i], m[i][j], m[j][-1-i], m[-1-i][-1-j] 

    print_matrix(m)
    return m

def print_matrix(matrix):
    for i in matrix:
        print(i)

class Test(unittest.TestCase):
    data = [
        ([ #5x5
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [21, 16, 11, 6, 1],
            [22, 17, 12, 7, 2],
            [23, 18, 13, 8, 3],
            [24, 19, 14, 9, 4],
            [25, 20, 15, 10, 5]
        ]),
	([ #4x4
	    [1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]
        ], [
            [13, 9, 5, 1],
	    [14, 10, 6, 2],
	    [15, 11, 7, 3],
	    [16, 12, 8, 4]
	]),
	([ #3x3
	    [1,2,3],
	    [4,5,6],
	    [7,8,9]
	], [
	    [7, 4, 1],
	    [8, 5, 2],
	    [9, 6, 3]
	]),
	([ #2x2
	    [1,2],
	    [3,4]
	], [
	    [3,1],
	    [4,2]
	]),
	([ #1x1
	    [1]
	], [
	    [1]
	]),
        ([ #0x0
            []
        ], [
            []
        ])
    ]

    def test_rotate_matrix(self):
    	for [m, expected] in self.data:
            actual = rotate_matrix(m)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

