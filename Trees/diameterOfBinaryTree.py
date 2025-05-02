# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Diameter of a binar Tree:
        Using DFS: inorder
        calculate each node's longest path which by summing up depth of left sub tree and right sub tree
        and check with the global value and update if the current depth value is less.
        base case: if node doesn't preset return 0
        when the node is present:
        left_depth = left sub tree
        right_depth = right sub tree
        total_depth = left_depth + right_depth
        max_depth = max(total_depth, max_depth)
        here  return 1+ max(right_depth,left_depth). #cal depth;
        """
        self.max_depth = 0
        def dfs(node):
            if not node:
                return 0
            if node:
                left_depth = dfs(node.left)
                right_depth = dfs(node.right)
                total_depth = left_depth + right_depth
                self.max_depth = max(total_depth,self.max_depth)
                return 1 + max(left_depth, right_depth)
        dfs(root)
        return self.max_depth
        