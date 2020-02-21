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
        stack = self.get_inorder(root)
        tar_pos = self.binary_search(stack, target)
        result = self.find_k_close(stack, target, tar_pos, k)
        return result
        
    def get_inorder(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        result, stack = [], [dummy]
        while stack:
            curr = stack.pop()
            if curr.right:
                curr = curr.right
                while curr:
                    stack.append(curr)
                    curr = curr.left
            if stack:
                result.append(stack[-1].val)
        return result
        
    def binary_search(self, arrary, target):
        left, right = 0, len(arrary) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if target < arrary[mid]:
                right = mid
            elif target > arrary[mid]:
                left = mid
            else:
                return mid
        return left if abs(arrary[left] - target) < abs(arrary[right] - target) else right
        
    def find_k_close(self, arrary, target, target_pos, k):
        left, right = target_pos-1, target_pos+1
        result = [arrary[target_pos]]
        while len(result) < k:
            if self.left_closer(arrary, left, right, target):
                result.append(arrary[left])
                left -= 1
            else:
                result.append(arrary[right])
                right += 1
        return result
        
    def left_closer(self, arrary, left, right, target):
        if left < 0:
            return False
        if right >= len(arrary):
            return True
        return abs(arrary[left] - target) < abs(arrary[right] - target)
        
        
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
        closest_node = self.find_closed_val(root, target)
        succesor = self.find_succesor(root, closest_node)
        precesor = self.find_precesor(root, closest_node)
        results = [closest_node.val]
        while len(results)<k:
            print(results)
            if succesor and precesor:
                if abs(succesor.val - target) < abs(precesor.val - target):
                    results.append(succesor.val)
                    succesor = self.find_succesor(root, succesor)
                else:
                    results.append(precesor.val)
                    precesor = self.find_precesor(root, precesor)
            elif not succesor:
                results.append(precesor.val)
                precesor = self.find_precesor(root, precesor)
            elif not precesor:
                results.append(succesor.val)
                succesor = self.find_succesor(root, succesor)
        return results
        
    def find_closed_val(self, root, target):
        lower, upper = root, root
        while root:
            if root.val > target:
                lower = root
                root = root.left
            elif root.val < target:
                upper = root
                root = root.right
            else:
                return root
        return upper if abs(upper.val - target) < abs(lower.val - target) else lower
        
    def find_succesor(self, root, node):
        ans = None 
        while root:
            if root.val > node.val:
                if not ans or ans.val > root.val:
                    ans = root
                root = root.left
            elif root.val < node.val:
                root = root.right
            elif root.val == node.val:
                root = root.right
        return ans 
        
    def find_precesor(self, root, node):
        ans = None 
        while root:
            if root.val > node.val:
                root = root.left
            elif root.val < node.val:
                if not ans or ans.val < root.val:
                    ans = root
                root = root.right
            elif root.val == node.val:
                root = root.left
        return ans 
          
        
    
