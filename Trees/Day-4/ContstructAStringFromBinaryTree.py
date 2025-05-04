# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: str
        """
        """
        String: concatication more easy and efficent, adding substrings to the list
        joining at the end.
        Traversal PreOrder:
        if the left node is not present I have to add the empty string().
        """
        result = []
        def preOrder(root):
            if not root:
                return
            result.append("(")
            result.append(str(root.val))
            if not root.left and root.right:
                result.append("()")
            preOrder(root.left)
            preOrder(root.right)
            result.append(")")
        preOrder(root)
        return "".join(result)[1:-1]
        