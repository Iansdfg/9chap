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
    average = float('-inf')  
    node = None
    def find_subtree2(self, root):
        # write your code here
        self.dfs(root)
        return self.node

    def dfs(self, root):
        if not root:
            return 0, 0

        left_sum, left_size = self.dfs(root.left)
        right_sum, right_size = self.dfs(root.right)

        summ = left_sum + right_sum + root.val
        size = right_size + left_size + 1

        # print(root.val, summ * 1.0/size)
        if self.average < summ * 1.0/size:
            self.average = summ * 1.0/size
            self.node = root 

        return summ, size


