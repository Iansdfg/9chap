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
    def closestKValues(self, root, target, k):
        # write your code here
        closest = self.find_closest(root, target)
        # print('closest: ', closest.val)
        successor = self.find_successor(root, closest)
        # print('successor: ', successor.val)
        predesessor = self.find_predesessor(root, closest)
        # print('predesessor: ', predesessor.val)
        
        results = [closest.val]
    
        while len(results) < k:
            if successor and predesessor :
                if abs(successor.val - target) < abs(predesessor.val - target):
                    results.append(successor.val)
                    successor = self.find_successor(root, successor)
                else:
                    results.append(predesessor.val)
                    predesessor = self.find_predesessor(root, predesessor)
            elif successor:
                results.append(successor.val)
                successor = self.find_successor(root, successor)
            elif predesessor:
                results.append(predesessor.val)
                predesessor = self.find_predesessor(root, predesessor)
            
        return results
        
    def find_closest(self, root, target):
        upper, lower = root, root 
        while root:
            if root.val < target:
                lower = root
                root = root.right
            elif root.val > target:
                upper = root
                root = root.left
            else:
                return root
        return upper if abs(upper.val - target) <  abs(lower.val - target) else lower

    def find_successor(self, root, node):
        ans = None
        while root:
            if root.val <= node.val:
                root = root.right
            elif root.val > node.val:
                if not ans or ans.val > root.val:
                    ans = root
                root = root.left
        return ans
        
    def find_predesessor(self, root, node):
        ans = None
        while root:
            if root.val < node.val:
                if not ans or root.val > ans.val:
                    ans = root
                root = root.right
            elif root.val >= node.val:
                root = root.left
        return ans
        
        
       
        
        
        
