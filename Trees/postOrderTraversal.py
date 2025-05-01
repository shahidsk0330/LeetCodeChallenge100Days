# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        postOrder Traversal is a Depth First search Traversal method. It travers Lefttree -> RightTree -> Root val
        Since we are visiting every node of the tree: Time complexity O(N)
        In worst Case Space compleixty O(N) due recurssion stack and storage length
        """
        result = [] 
        def postOrder(root):
            if root:
                postOrder(root.left)
                postOrder(root.right)
                result.append(root.val)
        postOrder(root)
        return result
        