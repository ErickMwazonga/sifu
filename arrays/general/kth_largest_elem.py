def find_Kth_largest(nums, k):
    nums.sort()
    n = len(nums)

    if k == 1:
        return nums[-1]

    return nums[n - k]


def find_Kth_largest2(nums, k):
    res = sorted(nums, reverse=True)
    return res[k - 1]


nums = [56, 14, 7, 98, 32, 12, 11, 50, 45, 78, 7, 5, 69]
assert find_Kth_largest(nums) == 5
assert find_Kth_largest2(nums) == 5
