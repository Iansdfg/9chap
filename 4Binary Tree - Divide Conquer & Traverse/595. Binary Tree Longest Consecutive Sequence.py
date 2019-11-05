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
        return self.helper(root, None, 0)
        
        
    def helper(self, root, parent, length):
        if not root:
            return 0

        if parent and root.val == parent.val + 1:
            length += 1
        else:
            length = 1
            
        left = self.helper(root.left, root, length)
        right = self.helper(root.right, root, length)
        
        return max(left, right, length)
        
