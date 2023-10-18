# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    RES = 0
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, root.val)
        return self.RES

    def dfs(self, node, max_val):
        if not node:
            return None

        if node.val >= max_val:
            self.RES += 1 
        max_val = max(max_val, node.val)

        self.dfs(node.left, max_val)
        self.dfs(node.right, max_val)

        
