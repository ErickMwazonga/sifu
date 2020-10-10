"""
Minimum rotations required to get the same string
Given a string, we need to find the minimum number of rotations required to get the same string.

Input : s = "geeks" -> 5
Input : s = "aaaa" -> 1
"""

def findRotations(str): 
      
    # tmp is the concatenated string. 
    tmp = str + str
    n = len(str) 
  
    for i in range(1, n + 1): 
        # substring from i index of original string size. 
        substring = tmp[i: n] 
  
        # if substring matches with original string then we will  
        # come out of the loop. 
        if (str == substring): 
            return i 
    return n

def findRotations2(_str):
    check = ''
    for r in range(1, len(_str) + 1):
        check = _str[r:] + _str[:r]
        if check == _str:
            return r


