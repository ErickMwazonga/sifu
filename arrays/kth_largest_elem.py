def findKthLargest(self, nums, k):
    nums.sort()

    if k == 1:
      return nums[-1]

    return nums[len(nums) - k]

assert findKthLargest([56, 14, 7, 98, 32, 12, 11, 50, 45, 78, 7, 5, 69]) == 5


def findKthLargest(self, nums: List[int], k: int) -> int:
    res = sorted(nums, reverse=True)
    return res[k - 1]