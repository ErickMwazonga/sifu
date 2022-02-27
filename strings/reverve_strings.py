'''
Write a function that takes a list of characters
and reverses the letters in place.

Careful: 'In-place' does not mean 'without creating any additional variables!'
Rather, it means 'without creating a new copy of the input.'
In general, an in-place function will only
create additional variables that are O(1) space.
'''


def reverse(chars: list):
    '''
    We swap the first and last characters,
    then the second and second-to-last characters, and so on until we reach the middle.
    O(n) time and O(1)O(1) space.
    '''

    left_index = 0
    right_index = len(chars) - 1

    while left_index < right_index:
        # Swap characters
        chars[left_index], chars[right_index] = chars[right_index], chars[left_index]

    # Move towards middle
    left_index += 1
    right_index -= 1
