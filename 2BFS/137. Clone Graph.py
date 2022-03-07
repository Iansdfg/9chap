


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

        root = UndirectedGraphNode(node.label)
        queue = deque([node])
        #we add node to dict b/c in bfs all pop item is visited
        #except the first one
        ori_clo = {}
        ori_clo[node] = root

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in ori_clo:
                    neighbor_clo = UndirectedGraphNode(neighbor.label)
                    ori_clo[neighbor] = neighbor_clo
                    queue.append(neighbor)
                ori_clo[curr].neighbors.append(ori_clo[neighbor])

        return root




