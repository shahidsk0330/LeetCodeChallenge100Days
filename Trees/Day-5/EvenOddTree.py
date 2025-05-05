# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        

        if not root:
            return True
        q = deque([root])
        level=0
        while q:
            nums = []
            for _ in range(len(q)):
                node = q.popleft()
                if level %2 ==0:
                    if node.val %2 ==0:
                        return False
                else:
                    if node.val %2 ==1:
                        return False
                
                nums.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            for i in range(len(nums)-1):
                if level %2 ==0:
                    if nums[i] >= nums[i+1]:
                        return False
                else:
                    if nums[i] <= nums[i+1]:
                        return False
            level+=1
        return True