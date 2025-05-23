# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root.left and not root.right:
            return root.val == 1
        if root.val == 2:
            return (self.evaluateTree(root.left) or self.evaluateTree(root.right))
        
        if root.val == 3:
            return (self.evaluateTree(root.left) and self.evaluateTree(root.right))
        