# Implement binary search to find a given element in a sorted array.

def binary_search(nums: list[int], target: int) -> bool:
	return traverse(nums, target, 0, len(nums) - 1)

def traverse(nums: list[int], target: int, left: int, right: int) -> bool:
	mid: int = (left + right) // 2

	if left > right:
		return False

	if nums[mid] == target:
		return True

	if nums[mid] > target:
		return traverse(nums, target, left, mid - 1)
	else:
		return traverse(nums, target, mid + 1, right)


assert binary_search([1, 2, 3, 4, 5, 6], 10) == False
assert binary_search([1, 2, 3, 4, 5, 6], 6) == True
