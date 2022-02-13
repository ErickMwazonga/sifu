'''
First repeating character
Given a string str, create a function that returns the first repeating character.
If such character doesn't exist, return the null character '\0'.

Examples
1. 'inside code' -> 'i'
2. 'programming' -> 'r'
3. 'abcd' -> None
'''


def first_repeating_character(str):
    seen = set()

    for char in str:
        if char in seen:
            return char

        seen.add(char)

    return None


first_repeating_character('inside code') == 'i'
first_repeating_character('programming') == 'r'
first_repeating_character('abcd') == None
