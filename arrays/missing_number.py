"""
https://www.geeksforgeeks.org/find-the-missing-number/
Find the Missing Number
You are given a list of n-1 integers and these integers are in the range of 1 to n.
There are no duplicates in the list. One of the integers is missing in the list. 
Write an efficient code to find the missing integer.

Example :
Input: arr[] = {1, 2, 4, 6, 3, 7, 8}
Output: 5

Input: arr[] = {1, 2, 3, 5}
Output: 4
"""

def get_missing(A): 
    length = len(A) + 1
    total = length * (length + 1) // 2

    sum_of_A = sum(A) 
    return total - sum_of_A

def get_missing1(A):
    """
    1) XOR all the array elements, let the result of XOR be X1.
    2) XOR all numbers from 1 to n, let XOR be X2.
    3) XOR of X1 and X2 gives the missing number
    """
    xor_some = A[0]
    xor_all = 1
    n = len(A)

    # Compute XOR of all elements in array
    for i in range(1, n): # Start from 1 since xor_some is initialized with first element
        xor_some ^= A[i]
    # Compute XOR of all elements in from 1 to n+1
    for i in range(2, n+2): 
        # Start from 2 since we are starting from number 2 remember the array doesn't have zero 
        # End at the length + 1 since it is less on, to include it in range +1
        xor_all ^= i
    return xor_all ^ xor_some


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

arr = [1, 2, 4, 5, 6]
print(get_missing1(arr))

