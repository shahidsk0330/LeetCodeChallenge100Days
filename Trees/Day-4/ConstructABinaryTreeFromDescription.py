# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def createBinaryTree(self, descriptions):
        """
        :type descriptions: List[List[int]]
        :rtype: Optional[TreeNode]
        """
        """
        Additionally we use here Hashmap and Hashset
        Hashmap: To track the parent node is present are not and as child node is present or not
        if parent is present in the hasmap then we add its new child node to the parent node adress which we get form hashmap.
        if child node is present then we extract the child node address from the hashmap and we add to parent.
        To find the final parent we added all the childs to the hashset and if we didn't find the child node then its the parent node.
        Total complexity: O(n) Space O(n)
        """
        nodes ={}
        children =set()

        for parent, child, is_left in descriptions:
            children.add(child)
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            if is_left == 1:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        for p, c, is_left in descriptions:
            if p not in children:
                return nodes[p]