# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = deque()
        result =[]
        if root:
            d.append(root)
        while(len(d) > 0):
            level =[]
            for i in range(len(d)):
                c = d.popleft()
                level.append(c.val)
                if(c.left != None):
                    d.append(c.left)
                if(c.right != None):
                    d.append(c.right)
            result.append(level)
        return result