# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        q = deque([root])
        level = 1
        while q:
            nums=[]
            for _ in range(len(q)):
                node = q.popleft()
                nums.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level %2 ==0:
                nums = nums[::-1]
            result.append(nums)
            level+=1
        return result