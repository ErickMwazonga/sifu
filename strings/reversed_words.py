'''
Write a function reverse_words() that takes a message
as a list of characters and reverses the order of the words in place.

message = [ 
    'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ',  's', 't', 'e', 'a', 'l'
]

reverse_words(message) -> 'steal pound cake'
'''


from typing import NoReturn


def reverse_words(message: list[str]) -> None:
    '''O(n) time and O(1) space!'''

    n = len(message)

    # First we reverse all the characters in the entire message
    reverse_characters(message, 0, n-1)

    # This gives us the right word order but with each word backward
    # Now we'll make the words forward again by reversing each word's characters

    # We hold the index of the *start* of the current word
    # as we look for the *end* of the current word
    current_word_start_index = 0

    for i in range(n + 1):
        # Found the end of the current word!
        if i == n or message[i] == ' ':
            reverse_characters(message, current_word_start_index, i - 1)
            # If we haven't exhausted the message our
            # next word's start is one character ahead
            current_word_start_index = i + 1


def reverse_characters(message: list[str], left: int, right: int) -> None:
    while left < right:
        # Swap the left char and right char
        message[left], message[right] = message[right], message[left]
        left, right = left + 1, right - 1
