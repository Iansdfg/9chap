# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    RES = 0
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, [])
        return self.RES


    def dfs(self, node, path):
        if not node:
            return None

        # print(node.val, path)
        if not path:
            self.RES += 1 
        if path and node.val >= max(path):
            self.RES += 1 
        path.append(node.val)
        self.dfs(node.left, path)
        self.dfs(node.right, path)
        path.pop()
        
