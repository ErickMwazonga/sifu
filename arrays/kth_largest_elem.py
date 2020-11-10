def findKthLargest(nums, k):
    nums.sort()
    n = len(nums)

    if k == 1:
      return nums[-1]

    return nums[n - k]

assert findKthLargest([56, 14, 7, 98, 32, 12, 11, 50, 45, 78, 7, 5, 69]) == 5


def findKthLargest(nums, k):
    res = sorted(nums, reverse=True)
    return res[k - 1]