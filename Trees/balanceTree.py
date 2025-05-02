# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Using DFS:
        base case: when the node is none : return 0 and true
        if the node is none:
            calculate ldepth and rdepth
            find the diff and check the sub tree is balance or not 
            return depth and balance or not
        """
        def dfs(root):
            if not root:
                return 0,True
            if root:
                ldepth,balance_left = dfs(root.left)
                rdepth, balance_right = dfs(root.right)
                balance = True if abs(ldepth-rdepth) <=1 and balance_left and balance_right else False
                return 1 + max(ldepth, rdepth), balance
        depth,balance = dfs(root)
        return balance