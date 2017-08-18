#!/usr/bin/python3

'''
Q1.9 String Rotation: 
    Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
'''

import unittest

#rs - rotated string
def string_rotation(s, rs):
    if len(s) != len(rs) or len(s) == 0:
        return False
    rsrs = rs + rs
    return is_substring(rsrs, s):

#if subtring found, return True
def is_substring(string, sub):
    return string.find(sub) != -1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
	("hahaboohoohaha", "ahahahaboohooh", True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
