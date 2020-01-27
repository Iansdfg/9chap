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
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        min_sum, mini_node, summ = self.helper(root)
        return mini_node
        
    def helper(self, root):
        # return min_sum, mini_node, summ
        if not root:
            return float('inf'), None, 0
        
        left_min_sum, left_mini_node, left_summ = self.helper(root.left)
        right_min_sum, right_mini_node, right_summ = self.helper(root.right)
        
        summ = left_summ + right_summ + root.val
        min_sum = min(summ, left_min_sum, right_min_sum)
        
        if left_min_sum == min_sum:
            return min_sum, left_mini_node, summ
        if right_min_sum == min_sum:
            return min_sum, right_mini_node, summ
        return min_sum, root, summ
