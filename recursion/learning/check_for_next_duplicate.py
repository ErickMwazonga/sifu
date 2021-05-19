'''
Given a string s, create a recursive boolean function that
checks if it has adjacent duplicates

Examples
'programming' -> True ...'mm'
'ababa' -> False
'pssst' -> True
'''

def hasAdjacentDuplicates(s, i=0):
    if i >= len(s) - 1:
        return False
    elif s[i] == s[i+1]:
        return True
    else:
        return hasAdjacentDuplicates(s, i+1)