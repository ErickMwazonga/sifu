'''
Given a string s, create a recursive boolean function that
checks if it has adjacent duplicates

Examples
1. 'programming' -> True ...'mm'
2. 'ababa' -> False
3. 'pssst' -> True
'''


def hasAdjacentDuplicates(s: str, i: int = 0) -> bool:
    if i >= len(s) - 1:
        return False
    
    if s[i] == s[i+1]:
        return True
    
    return hasAdjacentDuplicates(s, i+1)
