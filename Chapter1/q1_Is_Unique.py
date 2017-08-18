#!/usr/bin/python3

"""
Q1.1
    Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 
"""

def isUniqueDict(word):
    dict = {}
    for c in word:
        if(c in dict.keys()):
            return False
        else:
          dict[c] = True
    return True

def isUniqueNoDS(word):
    for c1 in word:
        count = 0
        for c2 in word:
            if c1 == c2:
                count += 1
            if count > 1:
                return False
    return True

#TEST
def main():
    print("alice",isUniqueDict("alice")) #True
    print("bob",isUniqueDict("bob")) #False

    print("alice",isUniqueDict("alice")) #True
    print("bob",isUniqueDict("bob")) #False

main()
