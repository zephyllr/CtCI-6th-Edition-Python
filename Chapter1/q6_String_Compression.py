#!/usr/bin/python

"""
Q1.6
    String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed"string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

import unittest

def str_compression(s):
    curr = s[1]
    count = 0
    comp_s = []

    for i in range(len(s)):
        if s[i] == curr:
            count += 1
        else:
            comp_s.extend([s[i-1], str(count)])
            curr = s[i]
            count = 1
    
    comp_s.extend([s[-1], str(count)])
    comp_s = "".join(comp_s)
    
    return min(s, comp_s, key=len)

#-------------------------------------------------
class Test(unittest.TestCase):
    #Test Case - Compressesed
    dataT = [
        ("aabbbcccccaa", "a2b3c5a2"),
        ("lloooddddfNNNNNnnddd", "l2o3d4f1N5n2d3")]
    #Test Case - Uncompressed
    dataF = [
        ("abcdefghijklmn"),
        ("abc")]
    #Test 1
    def test_compressed(self):
        for [s, expected] in self.dataT:
            actual = str_compression(s)
            self.assertEqual(actual, expected)
    #Test 2
    def test_uncompressed(self):
        for s in self.dataF:
            actual = str_compression(s)
            self.assertEqual(actual, s)

if __name__ == "__main__":
    unittest.main()

