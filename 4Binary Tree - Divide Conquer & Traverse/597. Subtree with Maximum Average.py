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
    @return: the root of the maximum average of subtree
    """
    max_avg = float('-inf')
    target_node = None  
    def findSubtree2(self, root):
        # write your code here
        summ, num = self.helper(root)
        return self.target_node
        
    def helper(self, root):
        # return sum and # of Node 
        if not root:
            return 0, 0
            
        left_sum, left_num = self.helper(root.left)
        right_sum, right_num = self.helper(root.right)
        
        summ = left_sum + right_sum + root.val 
        num = left_num + right_num + 1
        print(summ, num)
        
        avg = summ/num
        self.max_avg = max(self.max_avg, avg)
        if self.max_avg == avg:
            self.target_node = root
        
        return summ, num
        
        
        
