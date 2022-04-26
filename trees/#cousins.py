'''
993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
Return true if and only if the nodes corresponding to the values x and y are cousins.
'''


def isCousins(root, x: int, y: int) -> bool:
    res = []  # store (parent, depth) tuple

    queue = [(root, None, 0)]  # bfs
    while queue:
        # minor optimization to stop early if both targets found
        if len(res) == 2:
            break
        node, parent, depth = queue.pop(0)

        # if target found
        if node.val == x or node.val == y:
            res.append((parent, depth))
        if node.left:
            queue.append((node.left, node, depth + 1))
        if node.right:
            queue.append((node.right, node, depth + 1))

    # unpack two nodes
    node_x, node_y = res

    # compare and decide whether two nodes are cousins
    return node_x[0] != node_y[0] and node_x[1] == node_y[1]
