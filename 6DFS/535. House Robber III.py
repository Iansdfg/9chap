"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        # write your code here
        rob, not_rob = self.helper(root)
        return max(rob, not_rob)
        
        
    def helper(self, root):
        # return rob, not_rob
        if not root:
            return 0, 0
            
        left_rob, left_not_rob = self.helper(root.left)
        right_rob, right_not_rob = self.helper(root.right)
        
        rob = left_not_rob + right_not_rob + root.val
        not_rob = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)
        
        return rob, not_rob
