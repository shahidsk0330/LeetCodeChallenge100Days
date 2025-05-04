# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root,0)])
        hashmap = defaultdict(list)
        max_col,min_col = 0, 0
        while queue:
            node, col = queue.popleft()
            min_col, max_col = min(min_col, col), max(max_col, col)
            hashmap[col].append(node.val)
            if node.left:
                queue.append((node.left, col-1))
            if node.right:
                queue.append((node.right, col+1))
        return [hashmap[col] for col in range(min_col, max_col+1)]

