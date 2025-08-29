'''
Count Vowels in Substrings
https://www.hellointerview.com/learn/code/prefix-sum/count-vowels

Write a function to efficiently count vowels within specified substrings of a given string.
The substrings will be given to you a list queries of [left, right] pairs, which correspond to the substring word[left:right + 1] in Python.

The function should return a list of integers, where each integer represents the vowel count for the corresponding query. 
You can assume the input string will only contain lowercase letters.
Your function should be optimized to run efficiently for a large number of queries.

Input:
word = 'prefixsum'
queries = [[0, 2], [1, 4], [3, 5]]
Output: [1, 2, 1]

Explanation:
word[0:3] -> 'pre' contains 1 vowels
word[1:5]-> 'refi' contains 2 vowels
word[3:6]-> 'fix' contains 1 vowels
'''

def vowelStrings(word: str, queries: list[list[int]]):
    vowels = set('aeiou')
    n = len(word)

    # build prefix sum
    prefix = [0] * (n + 1)
    for i in range(0, n):
        prefix[i + 1] = prefix[i] + word[i] in vowels
        # prefix[i + 1] = prefix[i] + (1 if word[i] in vowels else 0)

    # work on queries
    res = []
    for start, end in queries:
        res.append(prefix[end + 1] - prefix[start])

    return res

def vowelStringsV2(word: str, queries: list[list[int]]):
    vowels = set('aeiou')
    prefix_sum = [0] * (len(word) + 1)

    # Part 1: create the prefix sum array
    for i in range(1, len(word) + 1):
        is_vowel = word[i - 1] in vowels
        prefix_sum[i] = prefix_sum[i - 1] + (1 if is_vowel else 0)

    # Part 2: calculate the number of vowels in each query 
    result = []
    for left, right in queries:
        num_vowels = prefix_sum[right + 1] - prefix_sum[left]
        result.append(num_vowels)

    return result
        