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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here 
        if not root:return []
        res = [[root.val]]
        queue = collections.deque()
        queue.append(root)
        while queue:
            queue_len = len(queue)
            path = []
            for i in range(queue_len):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                    path.append(curr_node.left.val)
                if curr_node.right:
                    queue.append(curr_node.right)
                    path.append(curr_node.right.val)
            if path != []:
                res.append(path)
        return res
