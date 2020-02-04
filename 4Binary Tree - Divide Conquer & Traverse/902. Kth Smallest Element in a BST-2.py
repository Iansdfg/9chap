"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        
        while k:
            curr = stack.pop()
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
                    
            if stack:
                res = stack[-1].val 
            k-=1
        
        return res 
                
        
        
                    
        
        
    
