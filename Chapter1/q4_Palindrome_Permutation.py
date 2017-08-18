#!/usr/bin/python3

"""
Q1.4
    Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. 
    A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.The palindrome does not need to be limited to just dictionary words.
"""

import unittest

def is_palindrome(s):
    return s == s[::-1]

def permutation_palindrome(s):
    penalty = 0
    charaCount = {i:0 for i in "abcdefghijklmnopqrstuvwxyz "}
    s = s.lower()
    for i in s:
        charaCount[i] += 1
    for k,v in charaCount.items():
        if k == ' ':
            continue
        if v % 2 != 0: 
            penalty += 1
            if penalty > 1:
                return False
    return True

#TEST
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = permutation_palindrome(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
