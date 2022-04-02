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
        return self.dfs(n, 1, n)


    def dfs(self, n, start, end):
        if start > end:
            return [None]

        res = []

        for rool_val in range(start, end + 1):
            left_trees = self.dfs(n, start, rool_val-1)
            right_trees = self.dfs(n, rool_val+1, end)

            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(rool_val)
                    root.left = left_tree
                    root.right = right_tree
                    res.append(root)

        return res 
            

