# Calculate the product of all elements in a given array.

def product(nums: list[int]) -> int:
	if len(nums) == 0:
		return 1

	return nums[0] * product(nums[1:])

def product_v2(nums: list[int]) -> int:
	def dfs(nums: list[int], index: int) -> int:
		if index == len(nums) - 1:
			return nums[index]
		
		return nums[index] * dfs(nums, index + 1)
	
	return dfs(nums, 0)

assert product([1, 2, 3, 4]) == 24