'''
LeetCode 1165. Single-Row Keyboard
PREMIUM

Description
https://leetcode.com/problems/single-row-keyboard/

There is a special keyboard with all keys in a single row.
Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
initially your finger is at index 0. To type a character,
you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

Example 1:
Input: keyboard = 'abcdefghijklmnopqrstuvwxyz', word = 'cba'
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4. 
'''


def calculate_time(keyboard: str, word: str) -> int:
    '''Time Complexity: O(N), Space Complexity: O(1)'''

    time = 0

    prev_index = 0
    for w in word:
        curr_idx = keyboard.index(w)
        time += abs(curr_idx - prev_index)
        prev_index = curr_idx

    return time
