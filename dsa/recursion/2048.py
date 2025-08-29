def merger(arr: list[int], direction: str) -> list[int]:
	if direction == 'left':
		return merge(arr)

	if direction == 'right':
		right_reversed = list(reversed(arr))
		merged_right = merge(right_reversed)
		return list(reversed(merged_right))


def merge(arr):
	if len(arr) == 1:
		return arr

	# Recursively merge the first n-1 tiles of the array
	merged = merge(arr[:-1])

	# If the last tile matches the second-to-last tile in the merged array, add them up
	if arr[-1] == merged[-1] and arr[-1] != 0:
		merged[-1] *= 2
	else:
		# Otherwise, append the last tile to the merged array
		merged.append(arr[-1])
	return merged

'''
	[0] -> [0]
	[0, 2] -> [2, 0]
	[2, 0] -> [2, 0]
	[2, 2] -> [4, 0]
	[2, 4] -> [2, 4]
'''
assert merger([2, 2, 2, 2], 'left') == [4, 4, 0, 0]
assert merger([2, 0, 2, 2], 'left') == [2, 4, 0, 0]
assert merger([2, 4, 8, 12], 'left') == [2, 4, 8, 12]
assert merger([4, 4, 0, 0], 'left') == [8, 0, 0, 0]
assert merger([8, 0, 0, 0], 'left') == [8, 0, 0, 0]
assert merger([8, 0, 0, 8], 'left') == [16, 0, 0, 0]
assert merger([2, 2, 4, 4], 'right') == [0, 0, 4, 8]
