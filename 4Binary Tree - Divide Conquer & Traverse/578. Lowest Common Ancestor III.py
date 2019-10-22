# """
# Definition of TreeNode:
# class TreeNode:
#     def __init__(self, val):
#         this.val = val
#         this.left, this.right = None, None
# """


# class Solution:
#     """
#     @param: root: The root of the binary tree.
#     @param: A: A TreeNode
#     @param: B: A TreeNode
#     @return: Return the LCA of the two nodes.
#     """
#     def lowestCommonAncestor3(self, root, A, B):
#         # write your code here
#         if not self.check_exist(root, A) or not self.check_exist(root, B):
#             return None
#         return self.helper(root, A, B)
            
#     def helper(self, root, A, B):
#         if not root:
#             return None 
#         if root is A or root is B:
#             return root
            
#         left = self.helper(root.left, A, B)
#         right = self.helper(root.right, A, B)
        
#         if left and right:
#             return root
#         if not left and right:
#             return right
#         if not right and left:
#             return left
#         return None
        
#     def check_exist(self, root, target):
#         if not root:
#             return False
#         if root is target:
#             return True
#         return self.check_exist(root.left, target) or self.check_exist(root.right, target) 
    
    
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a, b, lca = self.helper(root, A, B)
        if a and b:
            return lca
        else:
            return None
        
        
        
    def helper(self, root, A, B):
        """
        return if A exist, if B exist, LCA
        """
        if not root:
            return False, False, None
        
        a_left, b_left, lca_left = self.helper(root.left, A, B)
        a_right, b_right, lca_right = self.helper(root.right, A, B)
        
        
        a_exist = a_left or a_right or A == root
        b_exist = b_left or b_right or B == root
        
        
        if A == root or B == root:
            return a_exist, b_exist, root
        
        if lca_left and lca_right:
            return a_exist, b_exist, root
        elif lca_left and not lca_right:
            return a_exist, b_exist, lca_left
        elif lca_right and not lca_left:
             return a_exist, b_exist, lca_right
        
        return a_exist, b_exist, None
        
            

        
        
        
        
        
        
        
        
        
        

        
