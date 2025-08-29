# Calculate the sum of all elements in a given array.

def _sum(nums: list[int]) -> int:
	if len(nums) == 0:
		return 0

	return nums[0] + _sum(nums[1:])

def _sum_v2(nums: list[int]) -> int:
	def dfs(nums: list[int], index: int) -> int:
		if index == len(nums) - 1:
			return nums[index]
		
		return nums[index] + dfs(nums, index + 1)
	
	return dfs(nums, 0)

assert _sum_v2([1, 2, 3]) == _sum([1, 2, 3]) == 6