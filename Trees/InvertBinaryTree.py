# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        According to the problem statement:
        Every nodes children Left and Right should be swap.
        Using Depth First Search, I will traversa tree
        base case is when ever node is not None then we apply
        swap logic and we call left subtree and right subtree to do the same.
        """
        """
        Using Breadth First Search
        we use a queue to store the children of node which helps to move to next level.
        After extracting a node: we apply swap logic.
        then we start inserting the childres of the left and right sub tree if they are exits.
        """
        def dfs(node):
            if node:
                node.left,node.right = node.right, node.left
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return root