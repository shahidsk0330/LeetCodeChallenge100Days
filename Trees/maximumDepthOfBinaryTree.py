# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Maximum Depth of Binary Tree:
        maximum depth of node will be maxium depth of leftsubtree and right subtree and plus one: 
        using: dfs traversal method
        base case is: if the node is not present then return 0 as value.
        if node is present calculate dpeth of left subtree and right subtree 
        we store left subtree depth, we store the right subtree depth
        and return max depth
        """
        if not root:
            return 0
        if root:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return 1 + max(left_depth,right_depth)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Maximum Depth of Binary Tree:
        maximum depth of node will be maxium depth of leftsubtree and right subtree and plus one: 
        using: dfs traversal method
        base case is: if the node is not present then return 0 as value.
        if node is present calculate dpeth of left subtree and right subtree 
        we store left subtree depth, we store the right subtree depth
        and return max depth
        """
        """
        Using the BFS: 
        initialize the level=0
        base case: if root node exits then only we add into queue.
        untill queue has elements traverse.
        we increase the level when we move to next level.
        pop the elements and add its childs which are valid , to the queue.
        """
        level = 0
        queue = deque()
        if not root:
            return level
        else:
            queue.append(root)
        while queue:
            level +=1
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return level
