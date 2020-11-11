"""
Question - Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

def threeSum(nums):
    nums.sort()
    lis, n = [], len(nums)
  
    for i in range(n-2):
        low = i + 1
        high = n - 1
        
        while (low < high):
            s = nums[i] + nums[low] + nums[high]
            
            if s == 0:
                lis.append((nums[i], nums[low], nums[high]))
                low = low + 1
                high = high - 1
            if s < 0:
                low = low + 1
            if s > 0:
                high = high - 1
                
    res = list(set(lis))     
    res = [list(x) for x in res]
    return res

a = [-1, 0, 1, 2, -1, -4]

print(threeSum(a))
