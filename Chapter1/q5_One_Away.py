#!/usr/bin/python3

"""
Question 1.5
    One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""

import unittest

def one_away(str1, str2):
    if str1 == str2:
        return True

    str1L, str2L = len(str1), len(str2)
    diff = abs(str1L - str2L)

    if diff > 1:
        return False
    elif diff == 0:
        return checkEdit(str1, str2)
    elif str1L > str2L:
        return checkEdit(str1, str2)
    else:
        return checkEdit(str2, str1)
    return diff
            
def checkEdit(longer, shorter):
    if len(longer) == len(shorter):
        for i in range(len(longer)):
            if longer[i] != shorter[i]:
                if longer[i+1:] != shorter[i+1:]:
                    return False
                return True
    for i in range(len(shorter)):
        if shorter[i] != longer[i]:
            if shorter[i:] != longer[i+1:]:
                return False
            return True
    return True

#--------------------------------------------------
#TEST
class Test(unittest.TestCase):
    #Test Cases
    data = [
    	('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False),
        ("pale","ple", True)]

    def test_one_away(self):
        for [test_str1, test_str2, expected] in self.data:
            actual = one_away(test_str1, test_str2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
