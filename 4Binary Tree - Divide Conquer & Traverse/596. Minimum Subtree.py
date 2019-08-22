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
        mini_val, mini_root, summ = self.find_mini(root)
        
        return mini_root
        
    def find_mini(self, root):
        if not root:
            return float('inf'), None, 0
            
        left_mini_val, left_mini_root, left_summ = self.find_mini(root.left)
        right_mini_val, right_mini_root, right_summ = self.find_mini(root.right)
        
        curr_sum = root.val+right_summ+left_summ
        if left_mini_val == min(left_mini_val,right_mini_val,curr_sum):
            return left_mini_val, left_mini_root, curr_sum
        if right_mini_val == min(left_mini_val,right_mini_val,curr_sum):
            return right_mini_val, right_mini_root, curr_sum
            
        return curr_sum, root, curr_sum
            
            
