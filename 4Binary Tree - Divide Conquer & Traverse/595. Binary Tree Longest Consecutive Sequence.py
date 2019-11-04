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
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return self.helper(root, 0, None)
        
    def helper(self, root, lens, parent):
        if not root:
            return lens
            
        if parent and root.val == parent.val + 1:
            lens += 1
        else:
            lens = 1
            
        max_left_right = max(self.helper(root.left, lens, root), self.helper(root.right, lens, root))
        return max(lens, max_left_right)
        
