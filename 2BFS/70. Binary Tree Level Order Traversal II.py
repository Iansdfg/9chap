from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def level_order_bottom(self, root):
        # write your code here
        if not root:
            return [] 
        
        queue = [root]
        res = []
        while queue:
            next_q = []
            res = [[node.val for node in queue]]+ res
            for node in queue:
                
                if node.left:
                    next_q.append(node.left)
                if node.right:
                    next_q.append(node.right)

            queue = next_q
        return res 





        
