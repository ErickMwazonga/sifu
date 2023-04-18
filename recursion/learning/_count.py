# Count the number of elements in a given array.

def _count(nums: list[int | str]) -> int:
	N: int = len(nums)

	if N == 0 or N == 1:
		return N

	return 1 + _count(nums[1:])

assert _count([1, 2, 3, 4]) == 4