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
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closest_k_values(self, root, target, k):
        # write your code here
        closest_node = self.find_closest(root, target)
        next_node = self.inorderSuccessor(root, closest_node)
        prev_node = self.inorderPredecessor(root, closest_node)
        res = [closest_node.val]
        
        while len(res) < k:
        
            if next_node and prev_node:
                if abs(next_node.val - target) > abs(prev_node.val - target):
                    res.append(prev_node.val)
                    prev_node = self.inorderPredecessor(root, prev_node)
                else:
                    res.append(next_node.val)
                    next_node = self.inorderSuccessor(root, next_node)

            elif next_node:
                res.append(next_node.val)
                next_node = self.inorderSuccessor(root, next_node)

            elif prev_node:
                res.append(prev_node.val)
                prev_node = self.inorderPredecessor(root, prev_node)

        return res

    def find_closest(self, root, target):
        upper, lower = root, root

        while root:
            if root.val > target:
                upper = root
                root = root.left
            elif  root.val < target:
                lower = root
                root = root.right 
            else: 
                return root
        if abs(upper.val - target) > abs(lower.val - target):
            return lower
        else:
            return upper

    def inorderSuccessor(self, root, p):
        # write your code here
        if not p:
            return None 
        res = None 
        while root:
            if root.val > p.val:
                res = root
                root = root.left 
            else:
                root = root.right
        return res

    
    def inorderPredecessor(self, root, p):
        # write your code here
        if not p:
            return None 
        res = None 
        while root:
            if root.val >= p.val:
                root = root.left 
            else:
                res = root
                root = root.right
        return res

    
