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


class Solution:

    def majority_element(self, nums: list[int]) -> list[int]:
        cand1, cand2 = self.get_candidates(nums)

        # return [x for x in (cand1, cand2) if nums.count(x) > len(nums) // 3]

        # Get the candidate no of occurrences
        count1, count2 = 0, 0
        for num in nums:
            count1 += 1 if num == cand1 else 0
            count2 += 1 if num == cand2 else 0

        # Verify if indeed they have occurrences greate than n/3
        ans = []
        athird = len(nums) // 3
        ans += [cand1] if count1 > athird else []
        ans += [cand2] if count2 > athird else []

        return ans

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
