"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """
    def searchNode(self, graph, values, node, target):
        # write your code here
        queue = deque([node])
        visited = set()
        while queue:
            curr = queue.popleft()
            if values[curr] == target:
                    return curr
            visited.add(curr)
            for neighbor in curr.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)

        return None

        
