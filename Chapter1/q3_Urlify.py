#!/usr/bin/python3

"""
Question 1.3 
    URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform this operation in place.)
"""

#Inplace solution
def urlify(string, length):
    #python strings are immutable -> convert to list
    string = list(string)
    true_index = len(string)
    for i in reversed(range(length)):
        if string[i] == ' ':
            string[true_index - 3 : true_index] = '%20'
            true_index -= 3
        else:
            string[true_index-1] = string[i]
            true_index -= 1
    return ''.join(string)   

#TEST
string = "Mr John Smith    "
length = 13
print(urlify(string,length))

"""
#Non-inplace solution
def urlify(string):
    strList = string.split()
    newStr = '%20'.join(strList)
    return newStr
"""

