'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Example:
Input:  [1, 2, 3, 4]
Output: [24, 12, 8, 6]

Note: Please solve it without division and in O(n).
'''


def product_except_self(nums):
    size = len(nums)
    output = [1] * size

    for i in range(1, size):
        output[i] = nums[i-1] * output[i-1]

    right_product = 1

    for i in range(size-1, -1, -1):
        output[i] = output[i] * right_product
        right_product = right_product * nums[i]

    return output


def product_except_self(nums):
    size = len(nums)

    left_products = [1] * size
    right_products = [1] * size
    output = [1] * size

    # Get the products before the current index
    for i in range(1, size):
        left_products[i] = nums[i-1] * left_products[i-1]

    # Get the products after the current index
    for i in range(size-2, -1, -1):
        right_products[i] = nums[i+1] * right_products[i+1]

    # Multiply the multiples
    for i in range(size):
        output[i] = left_products[i] * right_products[i]

    return output


assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
