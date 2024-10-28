'''
735. Asteroid Collision
Link - https://leetcode.com/problems/asteroid-collision/description/

We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and 
the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8, -8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10, 2, -5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

WALKTHROUGH
# empty stack -> append

# forward asteroid 
    # positive tos -> append
    # negative tos -> append

# backward asteroid
    # positive tos -> check of collisions
        # same values - nothing
        # tos is less - remove
    # negative tos -> append
'''


def asteroidCollision(asteroids: list[int]) -> list[int]:
    stack = []

    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
            continue

        if stack and stack[-1] < 0: 
            stack.append(asteroid)
            continue

        have_same_weight = False
        while stack and abs(asteroid) >= stack[-1] and not have_same_weight:
            if stack[-1] < 0:
                stack.append(asteroid)
                break
            elif abs(asteroid) == stack[-1]:
                stack.pop()
                have_same_weight = True
            elif abs(asteroid) > stack[-1]:
                stack.pop()

        if not stack and not have_same_weight: 
            stack.append(asteroid)
    
    return stack

def asteroidCollision_v1(asteroids: list[int]) -> list[int]:
    stack = []

    for a in asteroids:
        while stack and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                a = 0
            else:
                a = 0
                stack.pop()
        if a:
            stack.append(a)

    return stack

