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
    mini_sum = float('inf')
    mini_node = None 
    def findSubtree(self, root):
        # write your code here
        self.helper(root)
        return self.mini_node
        
    def helper(self, root):
        # return sum 
        if not root:
            return 0
            
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        
        summ = left_sum + right_sum + root.val 
        self.mini_sum = min(self.mini_sum, summ)
        if self.mini_sum == summ:
            self.mini_node = root

        return summ
