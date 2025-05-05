# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def minimumOperations(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(nums):
            ops = 0
            sorted_nums = sorted(nums)
            idx_nums = {n:i for i,n in enumerate(nums)}
            for i in range(len(nums)):
                if nums[i] != sorted_nums[i]:
                    j = idx_nums[sorted_nums[i]]
                    nums[i],nums[j] = nums[j], nums[i]
                    idx_nums[nums[i]] = i
                    idx_nums[nums[j]] = j
                    ops +=1
            return ops
        #empty Tree
        if not root:
            return 0
        #Not Empty Tree
        q = deque()
        q.append(root)
        swap = 0
        #Level Order Travels
        while q:
            nums = []
            for _ in range(len(q)):
                node = q.popleft()
                nums.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            swap += helper(nums)
        return swap

        