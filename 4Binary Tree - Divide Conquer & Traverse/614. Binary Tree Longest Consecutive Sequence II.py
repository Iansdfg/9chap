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
    def longestConsecutive2(self, root):
        # write your code here
        max_len, _, _ = self.helper(root)
        return max_len
        
    def helper(self, root):
        # return length, up, down
        if not root:
            return 0, 0, 0
        
        left_length, left_up, left_down = self.helper(root.left)
        right_length, right_up, right_down = self.helper(root.right)
        
        up, down = 0, 0
        if root.left and root.left.val + 1 == root.val:
            down = max(down, left_down+1)
        if root.left and root.left.val - 1 == root.val:
            up = max(up, left_up+1)
            
        if root.right and root.right.val + 1 == root.val:
            down = max(down, right_down+1)
        if root.right and root.right.val - 1 == root.val:
            up = max(up, right_up+1)
            
        length = max(left_length, right_length, up+down+1)
        
        return length, up, down
            
        
        
        
        
