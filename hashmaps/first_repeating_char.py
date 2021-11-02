'''
First repeating character
Given a string str, create a function that returns the first repeating character.
If such character doesn't exist, return the null character '\0'.

Examples
Input: str = "inside code"
Output: 'i'

Input: str = "programming"
Output: 'r'

Input: str = "abcd"
Output: '\0'
'''


def firstRepeatingCharacter(str):
    seen = set()

    for char in str:
        if char in seen:
            return char

        seen.add(char)

    return '\0'
