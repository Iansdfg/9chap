"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        end = self.helper(root)
        return root
        
    def helper(self, root):
        # return tail of child 
        if not root:
            return None 
            
        left_end = self.helper(root.left)
        right_end = self.helper(root.right)
        
        
        if left_end and right_end:
            left_end.right = root.right
            root.right = root.left
            root.left = None
            return right_end
            
        elif right_end:
            return right_end
            
        elif left_end:
            root.right = root.left
            root.left = None 
            return left_end
            
        else:
            return root 
