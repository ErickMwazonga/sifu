'''
Smallest number after removing k digits
Description
Given a positive integer k and string num that represents a positive integer,
create a function that returns as a string, the smallest number that can be made by removing k digits from num.
Note that both input and output don't contain leading zeroes, except for the number 0 itself.

Example 1:
    Input: num = "825563", k = 2
    Output: "2553"
Example 2:
    Input: num = "83866", k = 3
    Output: "36"
Example 3:
    Input: num = "20050", k = 1
    Output: "50"
'''


def smallestAfterRemoving(num, k):
    if k == len(num):
        return "0"
    stack = []

    for digit in num:
        while len(stack) > 0 and digit < stack[-1] and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)

    while k > 0:
        stack.pop()
        k -= 1

    stack = stack[::-1]
    while len(stack) > 0 and stack[-1] == "0":
        stack.pop()
    stack = stack[::-1]

    return "".join(stack) if len(stack) > 0 else "0"
