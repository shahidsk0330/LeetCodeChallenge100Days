# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        InOrder Traversal is a Depth first search traversal method: Where it 
        visits Left Tree ->  Root Node -> Right Tree. 
        In Binary search Trees  where it returns the node in sorted (ascending) ordrer
        #Here we will be visiting all the nodes in the tree: So the Time complexity is Big O(N) : N size of the tree.
        Space Complexity: O(N) due to recurssion stack or result storage.
        """
        result = []   # for storage
        def inOrder(root):
            #base case
            if root:
                inOrder(root.left)
                result.append(root.val)
                inOrder(root.right)
        inOrder(root)
        return result

        
