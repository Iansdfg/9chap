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
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum2(self, root, target):
        # write your code here
        combinations = []
        self.dfs(root, target, [], combinations)
        return combinations


    def dfs(self, root, target, combination, combinations):
        if not root:
            return 

        combination.append(root.val)

        for i in range(len(combination)):
            if sum(combination[i:]) == target:
                combinations.append(combination[i:])

        for next_node in [root.left, root.right]:
            self.dfs(next_node, target, combination, combinations)
        
        combination.pop()
