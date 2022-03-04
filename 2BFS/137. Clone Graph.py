from lintcode import (
    UndirectedGraphNode,
)

"""
Definition for a UndirectedGraphNode:
class UndirectedGraphNode:
    def __init__(self, label):
        self.label = label
        self.neighbors = []
"""
from collections import deque
class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def clone_graph(self, node):
        # write your code here
        if not node:
            return None 

        queue = deque([node])
        ori_clo = {}
        root = UndirectedGraphNode(node.label)
        ori_clo[node] = root

        while queue:
            ori_curr = queue.popleft()
            # print('label', ori_curr.label)

            for neighbor in ori_curr.neighbors:
                # print('neighbor', neighbor.label)
                if neighbor not in ori_clo:
                    ori_clo[neighbor] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)

                ori_clo[ori_curr].neighbors.append(ori_clo[neighbor])

        return root
