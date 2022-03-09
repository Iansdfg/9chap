from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    MAX = None
    AVG = float('-inf') 
    def find_subtree2(self, root):
        # write your code here
        self.dfs(root)
        return self.MAX

    def dfs(self, root):
        if not root:
            return 0, 0

        left_summ, left_num = self.dfs(root.left)
        right_summ, right_num = self.dfs(root.right)

        summ = left_summ + right_summ + root.val
        num = left_num + right_num + 1

        if self.AVG < summ * 1.0 / num :
            self.AVG = summ * 1.0 / num
            self.MAX = root

        return summ, num

