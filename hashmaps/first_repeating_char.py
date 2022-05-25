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


def first_repeating_character_v2(str):
    counter = {}

    for ch in str:
        counter[ch] = counter.get(ch, 0) + 1

    for k, v in counter.items():
        if v > 1:
            return k

    return None


assert first_repeating_character('inside code') == 'i'
assert first_repeating_character('programming') == 'r'
assert first_repeating_character('abcd') == None
