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
        # return len, upper_len, lower_len
        if not root:
            return 0, 0, 0
            
        left_len, left_up, left_down = self.helper(root.left)
        right_len, right_up, right_down = self.helper(root.right)
        
        up, down = 0, 0
        if root.left and root.left.val == root.val + 1:
            up = max(left_up + 1, up)
            
        if root.left and root.left.val == root.val - 1:
            down = max(left_down + 1, down)
        
        if root.right and root.right.val == root.val + 1:
            up = max(right_up + 1, up)
            
        if root.right and root.right.val == root.val - 1:
            down = max(right_down + 1, down)
            
            
        length = up + down + 1
        length = max(length, left_len, right_len)
        return length, up, down
        
        
        
