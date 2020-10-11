"""
https://www.geeksforgeeks.org/find-the-missing-number/
Find the Missing Number
You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list. 
Write an efficient code to find the missing integer.

Example :
Input: arr[] = {1, 2, 4, 6, 3, 7, 8} -> 5
Input: arr[] = {1, 2, 3, 5} -> 4
"""


def missingNumber(nums):
    n = len(nums)
    visited = set(nums)
    
    for i in range(0, n + 1):
        if i not in visited:
            return i

def get_missing(A): 
    length = len(A) + 1
    total = length * (length + 1) // 2

    sum_of_A = sum(A) 
    return total - sum_of_A


def get_missing_one(nums):
    """
    1) XOR all the array elements, let the result of XOR be X1.
    2) XOR all numbers from 1 to n, let XOR be X2.
    3) XOR of X1 and X2 gives the missing number
    """
    length = len(nums)
    xor_nums = nums[0]
    xor_all = 1 # xor_all = 0 if nums start @ 0

    # Compute XOR of all elements in array
    for i in range(1, length): # Start from 1 since xor_nums is initialized with first element
        xor_nums ^= nums[i]
    # Compute XOR of all elements in from 1 to n+1
    for i in range(2, length+2): # for i in range(1, length+1): if start @0
        # Start from 2 since we are starting from number 2 remember the array doesn't have zero 
        # End at the length + 1 since it is less on, to include it in range +1
        xor_all ^= i
    return xor_all ^ xor_nums


def get_missing_zero(nums):
    length = len(nums)
    xor_nums = nums[0]
    xor_all = 0

    for i in range(1, length):
        xor_nums ^= nums[i]
    for i in range(1, length+1):
        xor_all ^= i
    return xor_nums ^ xor_all


# Find missing between two given sets
def find_missing(full_list, partial_list):
    missing_nums = set(full_list) - set(partial_list)
    assert(len(missing_nums) == 1)
    return list(missing_nums)[0]


def find_missing1(full_list, partial_list):
    xor_sum = 0
    for num in full_list:
        xor_sum ^= num
    for num in partial_list:
        xor_sum ^= num
    return xor_sum


assert find_missing([0, 1, 2, 4, 5, 6]) = 7
assert find_missing([3,0,1]) = 2
assert find_missing([9,6,4,2,3,5,7,0,1]) = 8

