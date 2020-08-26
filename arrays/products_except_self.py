'''
238. Product of Array Except Self
Given an array nums of n integers where n > 1, 
return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of
any prefix or suffix of the array (including the whole array)
fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for
the purpose of space complexity analysis.)
'''


def productExceptSelf(nums):
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


assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]