"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        result = []
        self.post(root, result)
        return result
        
    def post(self, root, result):
        if not root:
            return
        
        self.post(root.left, result)
        self.post(root.right, result)
        result.append(root.val)
        
        
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        res, stack = [], []
        curr = root
        while curr:
            stack.append(curr)
            if curr.left:
                curr =  curr.left
            else:
                curr = curr.right
                
        while stack:
            
            curr = stack.pop()
            res.append(curr.val)

            if stack and stack[-1].left == curr:
                curr =  stack[-1].right
                while curr:
                    stack.append(curr)
                    if curr.left:
                        curr =  curr.left
                    else:
                        curr = curr.right     
        return res
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        return res
