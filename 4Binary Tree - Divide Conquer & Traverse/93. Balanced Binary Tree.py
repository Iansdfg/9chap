# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        h, is_balanced = self.helper(root)
        return is_balanced
        

    def helper(self, root):
        # height, is_balanced
        if not root:
            return 0, True
            
        left_height, left_is_balanced = self.helper(root.left)
        right_height, right_is_balanced = self.helper(root.right)
        
        height = max(left_height, right_height) + 1
        
        if not left_is_balanced or not right_is_balanced:
            return height, False
        
        is_balanced = False if abs(left_height - right_height)>1 else True
        
        return height, is_balanced
