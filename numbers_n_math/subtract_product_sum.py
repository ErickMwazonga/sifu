'''
1281. Subtract the Product and Sum of Digits of an Integer
https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Examples:
1. 234 -> 15 
Explanation: 
    Product of digits = 2 * 3 * 4 = 24 
    Sum of digits = 2 + 3 + 4 = 9 
    Result = 24 - 9 = 15
'''


def subtractProductAndSum(n: int) -> int:
    product = 1
    _sum = 0

    while n > 0:
        n, rem = divmod(n, 10)
        product *= rem
        _sum += rem

    return product - _sum


assert subtractProductAndSum(234) == 15
