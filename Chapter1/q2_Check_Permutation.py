#!/usr/bin/python3

"""
Question 1.2
    Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
Note: permutation -> when all charas in str1 are present in str2; order does not matter; whitespace matters; confirm if str is ascii
    
"""

#------------------------------------------------
#O(nlogn)
def permutation2(str1, str2):
    if len(str1) != len(str2):
        return False        
    return sorted(str1) == sorted(str2)

#------------------------------------------------
#O(n)
def permutation(str1, str2):
    str1Dict, str2Dict = {}, {}
    
    if len(str1) != len(str2):
        return False        

    for i in str1:
        if i in str1Dict.keys():
            str1Dict[i] += 1
        else:
            str1Dict[i] = 1
    for i in str2:
        if i in str2Dict.keys():
            str2Dict[i] += 1
        else:
            str2Dict[i] = 1

    if str1Dict == str2Dict:
        return True
    return False

#------------------------------------------------
def permutation3(str1, str2):
    charaCount = [0 for i in range(128)]
    for i in str1:
        charaCount[ord(i)] += 1
    for i in str2:
        charaCount[ord(i)] -= 1
        if charaCount[ord(i)] < 0:
            return False
    return True

#------------------------------------------------
#TEST
str1 = 'wef34 f'
str2 = 'wff e34'
str3 = 'dcw4f'
str4 = 'dcw5f'

print(permutation(str1,str2), "True")
print(permutation(str3,str4), "False")

print(permutation2(str1,str2), "True")
print(permutation2(str3,str4), "False")

print(permutation3(str1,str2), "True")
print(permutation3(str3,str4), "False")

