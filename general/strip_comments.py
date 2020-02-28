"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:
Given an input string of:
apples, pears # and bananas
grapes
bananas !apples

The output expected would be:
apples, pears
grapes
bananas
"""
import re

def solution(string, markers):
    markers = '|'.join(['{}{}'.format('\\', m) for m in markers])
    string_list = string.split('\n')

    res = []

    for i in string_list:
        uncommented = re.split(markers, i)[0]
        uncommented = uncommented.strip()

        res.append(uncommented)
    
    return '\n'.join(res)

# solution("a #b\nc\nd $e f g", ["#", "$"])

# solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")

solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]), 
# "apples, pears\ngrapes\nbananas")