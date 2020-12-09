'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2
'''

def subarraySum(nums, k):
    # first we start from a sum which is equal to 0, and the count of it is 1. 
    # this is the input list ex :   [1 4 9 -5 8] -> the sum array (s) ex : [0  1    5    13    8    16 ]    
    
    sumDict = {0: 1}
    n = len(nums)
    count = our_sum = 0 
    
    for num in nums:
        our_sum += num # cumilative sums, s:    

        # we make sure to check if the sum - k is already in the dictionary, if so, increase the count.         
        if our_sum - k in sumDict:
            count += sumDict[our_sum - k]

        # we check if s is already in the sumDict, if so, increase by 1, if not assign 1.             
        sumDict[s] = sumDict.get(our_sum, 0) + 1   

    # finally return the occurance    
    return count


def subarraySum2(self, nums: List[int], k: int) -> int:
    sums_so_far = defaultdict(int)
    our_sum = 0
    num_subarrays = 0
    
    for v in nums:
        our_sum += v
        
        if our_sum == k:
            num_subarrays += 1
            
        if our_sum - k in sums_so_far:
            num_subarrays += sums_so_far[our_sum - k]
            
        sums_so_far[our_sum] += 1
        
    return num_subarrays



def subarraySum(self, nums, k):
    count = {0: 1}
    cur, res = 0, 0

    for n in nums:
        cur += n
        gap = curr - k
        # res += count.get(cur - k, 0)
        if gap in count:
            res += count[gap]

        count[cur] = count.get(cur, 0) + 1
        
    return res