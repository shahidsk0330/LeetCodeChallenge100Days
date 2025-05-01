# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        PreOrder Traversal is belong to Depth First Traversal. In preOrder traversal we go Root val -> LeftTree -> Right Tree. 
        Since we are visiting every node in the tree: Time complexity O(N) N: size of the tree
        In worst case Space Complexity O(N) due to recurssion call and result storage.
        """
        result = []
        def preOrder(root):
            if root:
                result.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return result
        