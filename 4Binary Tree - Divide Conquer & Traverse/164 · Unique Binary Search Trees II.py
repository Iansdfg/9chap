"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        return self.dfs(1, n)

    def dfs(self, start, end):
        if start > end:
            return [None]
        res = []
        for root_val in range(start, end + 1):
            left_nodes = self.dfs(start, root_val - 1)
            right_nodes = self.dfs(root_val + 1, end)

            for left_node in left_nodes:
                for right_node in right_nodes:
                    curr = TreeNode(root_val)
                    curr.left = left_node
                    curr.right = right_node
                    res.append(curr)
        return res
        
