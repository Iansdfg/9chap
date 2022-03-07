

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
        ori_clo = {}
        root = UndirectedGraphNode(node.label)
        ori_clo[node] = root
        #we add node to dict b/c in bfs all pop item is visited
        #except the first one
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in ori_clo:
                    clo_neighbor = UndirectedGraphNode(neighbor.label)
                    ori_clo[neighbor] = clo_neighbor
                    queue.append(neighbor)

                ori_clo[curr].neighbors.append(ori_clo[neighbor])
        return root




