'''
House Robber III
https://leetcode.com/problems/house-robber-iii/
https://www.hrwhisper.me/leetcode-house-robber-iii/
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked
houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight
without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]
     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]
     3
    / \
   4   5
  / \   \ 
 1   3   1
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

E X P L A N A T I O N
Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]
'''


class Solution:
    def rob(self, root) -> int:
        return max(self.dfs(root))

    def dfs(self, root):
        '''[With Root, Without Root]'''

        if not root:
            return [0, 0]

        left_pair = self.dfs(root.left)
        right_pair = self.dfs(root.right)

        with_root = root.val + left_pair[1] + right_pair[1]
        without_root = max(left_pair) + max(right_pair)

        return [with_root, without_root]
