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
