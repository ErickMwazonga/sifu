# Find the minimum element in a given array.

def _min(nums: list[int]) -> int:
	if len(nums) == 1:
		return nums[0]

	sub_min = _min(nums[1:])
	return nums[0] if nums[0] > sub_min else sub_min

assert _min([2, 4, 6, 1]) == 6
