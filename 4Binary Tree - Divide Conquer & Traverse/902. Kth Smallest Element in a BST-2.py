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
        ans = None 
        for _ in range(k):
            curr = stack.pop()
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
            if stack:
                ans = stack[-1].val
                # print(ans.val)
        return ans 
    
    
    
# Require CRUD   
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
    node_to_count = dict()
    def kthSmallest(self, root, k):
        # write your code here
        self.count(root)
        return self.helper(root, k)
        
    def count(self, root):
        if not root:
            return 0
            
        left_count = self.count(root.left)
        right_count = self.count(root.right)
        
        summ = left_count + right_count + 1 
        self.node_to_count[root] = summ
        return summ
    
    
    def helper(self, root, k):
        
        left_count = self.count(root.left) if root.left else 0
        
        if k <= left_count:
            return self.helper(root.left, k)
        elif k == left_count+1:
            return root.val
        elif k > left_count+1:
            return self.helper(root.right, k - left_count - 1)
        
        
         
