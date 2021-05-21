"""
This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces), 
return the original sentence in a list.
If there is more than one possible reconstruction, return any of them. 
If there is no possible reconstruction, then return null.

For example,
given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox",
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def reconstruction(words, s):
    words = set(words)
    res = []

    n = len(s)
    i = j = 0

    while j < n:
        if s[i:j+1] in words:
            res.append(s[i:j+1])
            i = j + 1
        else:
            if j == n - 1:
                return None

        j += 1

    return res


dictionary = ['bed', 'bath', 'bedbath', 'and', 'beyond']
word = 'bedbathandbeyond'
result = [['bed', 'bath', 'and', 'beyond'], ['bedbath', 'and', 'beyond']]
assert reconstruction(dictionary, word) in result

dictionary = ['quick', 'brown', 'the', 'fox']
word = 'thequickbrownfox'
result = [['the', 'quick', 'brown', 'fox']]
assert reconstruction(dictionary, word) in result

dictionary = ['quick', 'the', 'fox']
word = 'thequickbrownfox'
assert reconstruction(dictionary, word) is None
