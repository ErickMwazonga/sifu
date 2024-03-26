'''
229. Majority Element II
Link: https://leetcode.com/problems/majority-element-ii/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?

Examples
1. [3, 2, 3] -> [3]
2. [1] -> [1]
3. [1, 2] -> [1, 2]
'''

from collections import Counter

def majorityElement(nums: list[int]) -> list[int]:
    counts = Counter(nums)
    threshold = len(nums) // 3
    majority_elements = []

    for num, frequency in counts.items():
        if frequency > threshold:
            majority_elements.append(num)

    return majority_elements
    # return [k for k, v in Counter(nums).items() if v > len(nums) // 3 ]


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        
        # First pass to find potential candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        
        # Second pass to verify candidates
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        threshold = len(nums) // 3
        result = []
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)
        
        return result


class Solution_V2:

    def majority_element(self, nums: list[int]) -> list[int]:
        candidate1, candidate2 = self.get_candidates(nums)
    
        counter1, counter2 = 0, 0
        for num in nums:
            if num == candidate1:
                counter1 += 1
            elif num == candidate2:
                counter2 += 1

        # Verify if indeed they have occurrences greate than n/3
        threshold = len(nums) // 3
        result = []
        if counter1 > threshold:
            result.append(candidate1)
        if counter2 > threshold:
            result.append(candidate2)

        return result

    def get_candidates(self, nums: list[int]) -> tuple[int | None, int | None]:
        cand1, count1 = None, 0
        cand2, count2 = None, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1, count2 = count1 - 1, count2 - 1

        return cand1, cand2


soln = Solution()
assert soln.majority_element([1, 2]) == [1, 2]
