# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        def reverse(node1, node2,depth):
            if not node1 and not node2:
                return
            if (depth % 2 == 1):
                node1.val, node2.val = node2.val, node1.val
            reverse(node1.left, node2.right, depth+1)
            reverse(node1.right, node2.left,depth+1)
        reverse(root.left, root.right, 1)
        return root
            