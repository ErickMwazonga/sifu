'''
443. String Compression
https://leetcode.com/problems/string-compression/

Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, 
be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.
 
Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
'''


def compress(chars) -> int:
    n = len(chars)

    if n == 1:
        return 1

    i, start, _count = 1, 0, 1
    length = 0

    while i < n:
        if chars[i] != chars[i-1]:
            print(i)
            chars[start+1] = str(_count)
            start, _count = i, 1
            length += 2
        else:
            _count += 1

        i += 1

    chars[start+1] = str(_count)
    length += 2
    chars = chars[:length]

    print(chars, length)

    return length


compress(["a", "a", "b", "b", "c", "c", "c"])
