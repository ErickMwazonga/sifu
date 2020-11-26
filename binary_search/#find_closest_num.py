# YouTube Video: https://www.youtube.com/watch?v=0gkWZNE1H4Y&list=PL5tcWHG-UPH1kjiE-Fqt1xCSkcwyfn2Jb
"""
Given an array of sorted integers. We need to find the closest value to the 
given number.
Array may contain duplicate values and negative numbers.
Examples:
    Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}
    Target number = 11
    Output : 9
    9 is closest to 11 in given array
    Input :arr[] = {2, 5, 6, 7, 8, 8, 9}
    Target number = 4
    Output : 5
    Given[1, 2, 3]and target =2, return1.

Given[1, 4, 6]and target =3, return1.
Given[1, 4, 6]and target =5, return1or2.
Given[1, 3, 3, 4]and target =2, return0or1or2.
"""

def closestNumber(A, target):
    if not A:
        return -1
    
    low, high = 0, len(A) - 1

    while low + 1 < high:
        mid = low + (high - low) // 2

        if A[mid] <= target:
            low = mid
        else:
            high = mid
        
    
    left = abs(A[low] - target)
    right = abs(A[high] - target)

    if left <= right:
        return low
     
    return high


A = [1, 2, 4, 5, 6, 6, 8, 9]
# A = [2, 5, 6, 7, 8, 8, 9]
print(closestNumber(A, 11))