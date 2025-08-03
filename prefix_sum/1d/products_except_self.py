'''
238. Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Example:
Input:  [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Note: Please solve it without division and in O(n).
'''


def product_except_self(nums):
    ''' 
    [Intuition - Prefix and Suffix Products]
    nums -  [1, 2, 3, 4]

    left -  [1, 1, 2, 6]
    right - [24, 12, 4, 1]

    Output: [24, 12, 8, 6]
    '''

    n = len(nums)

    left_products, right_products = [1] * n, [1] * n
    output = [1] * n

    # Get the products before the current index
    for i in range(1, n):
        left_products[i] = nums[i-1] * left_products[i-1]

    # Get the products after the current index
    for i in range(n-2, -1, -1):
        right_products[i] = nums[i+1] * right_products[i+1]

    # Multiply the multiples
    for i in range(n):
        output[i] = left_products[i] * right_products[i]

    return output


def product_except_self_v2(nums):
    n = len(nums)
    output = [1] * n

    # Get prefix products
    for i in range(1, n):
        output[i] = nums[i-1] * output[i-1]

    # Get suffix products and multiply with prefix products
    right_product = 1
    for i in range(n-1, -1, -1):
        output[i] = output[i] * right_product
        right_product = right_product * nums[i]

    return output


assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
