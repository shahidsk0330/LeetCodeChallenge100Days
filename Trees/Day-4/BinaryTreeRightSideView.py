# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        if not root:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            rightSide= None
            for i in range(len(queue)):
                node = queue.popleft()
                rightSide = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if rightSide:
                result.append(rightSide.val)
        return result

        