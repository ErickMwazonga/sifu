'''
https://leetcode.com/problems/valid-palindrome/
125. Valid Palindrome
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

"A man, a plan, a canal: Panama" -> true
"race a car" -> false
'''

def isPalindrome(self, s: str) -> bool:
    '''
    Time complexity: O(N), Space complexity: O(N)
    '''
    s = s.lower()
    left = right = ''
    
    for i in range(0, len(s)):
        if s[i].isalnum():
            left += s[i]
            
    return left == left[::-1]

def is_palindrome2(s):
    '''
    Time complexity: O(N), Space complexity: O(1)
    '''
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False 
        i += 1
        j -= 1

    return True


print(is_palindrome('pap'))