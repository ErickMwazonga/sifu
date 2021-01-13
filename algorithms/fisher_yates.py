'''
384. Shuffle an Array
https://leetcode.com/problems/shuffle-an-array/

Given an integer array nums, design an algorithm to randomly shuffle the array.
Implement the Solution class:
Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.
'''

# FISHER-YATES
def shuffle(A) -> List[int]:
    """
    Returns a random shuffling of the array.
    Inspired by - https://www.youtube.com/watch?v=4zx5bM2OcvA
    """
    
    last_index = len(A) - 1
    while last_index > 0:
        rand_index = random.randint(0, last_index)
        A[last_index], A[rand_index] = A[rand_index], A[last_index]
        last_index -= 1
    
    return A