'''
Queries to print the character that occurs the maximum number of times in a given range
https://www.geeksforgeeks.org/dsa/queries-to-print-the-character-that-occurs-the-maximum-number-of-times-in-a-given-range/

You are given a stringS of length N.
Given L and R, find the most common character in the substring S[L..R1. N, Q < = 100'000
'''

def solveQueries(s, queries):
    N = len(s)
    prefix = []

    # Build prefix frequency array using dictionaries
    freq = {chr(c): 0 for c in range(ord('a'), ord('z') + 1)}
    for i in range(N):
        freq[s[i]] += 1
        # Append a copy of the current frequency dict
        prefix.append(freq.copy())

    # Process each query
    res = []
    for idx, (l, r) in enumerate(queries): # time complexity O(Q)
        count = {}
        for c in freq: # time complexity O(26)
            right = prefix[r][c]
            left = prefix[l - 1][c] if l > 0 else 0
            count[c] = right - left

        # Find the character with the maximum count
        max_char = max(count, key=lambda k: (count[k], -ord(k)))  # ties go to lex smaller
        res.append(max_char)
    
    return res

def solveQueriesV2(s, queries):
    N = len(s)

    # Use 26 for lowercase letters 'a' to 'z'
    prefix = [[0] * 26 for _ in range(N)]

    # Build the prefix frequency array
    for i in range(N):
        char_idx = ord(s[i]) - ord('a')
        prefix[i][char_idx] += 1

        if i > 0: # avoid index error for i = 0
            for j in range(26):
                prefix[i][j] += prefix[i - 1][j]

    # Process each query
    res = []
    for idx, (l, r) in enumerate(queries):
        max_freq = 0
        max_char = 'a'

        for j in range(26):
            freq = prefix[r][j]
            if l > 0:
                freq -= prefix[l - 1][j]

            if freq > max_freq:
                max_freq = freq
                max_char = chr(j + ord('a'))

        res.append(max_char)
    
    return res