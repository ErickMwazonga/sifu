# Find the maximum element in a given array.

def _max(nums: list[int]) -> int:
	if len(nums) == 1:
		return nums[0]

	sub_max = sub_max(nums[1:])
	return nums[0] if nums[0] > sub_max else sub_max

assert _max([2, 4, 6, 1]) == 6