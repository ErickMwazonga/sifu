## Two Pointer iteration

```py
'''
[M A D A M]

i  0(M) 1(A) 2(D)
j  4(M) 3(A) 2(D)

string = 'madam'
            ji

string = 'friend'
          i    j
i = 0
last_index = len(nums)

ACCRA - CAPE - KUMASI (500 KM)
 X ->           <- Y

X == Y:
WHILE X <= Y
 DRIVING
'''

def is_palindrome(string: str) -> bool:
    if not string:
        return True

    i, j = 0, len(string) - 1
    while i <= j:
        if string[i] == string[j]:
            continue
            # return True  # MABAAM

        if string[i] != string[j]:
            return False

        i += 1
        j -= 1

    return True
```

344. Reverse String
     Link - https://leetcode.com/problems/reverse-string/description/

Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ['h','e','l','l','o']
Output: ['o','l','l','e','h']

Example 2:
Input: s = ['H','a','n','n','a','h']
Output: ['h','a','n','n','a','H']

```py
def reverseString(s):
    #    i, j = 0, len(s)
    #    while i < j:

    i, j = 0, len(s) - 1
    while i <= j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

    return s
```
