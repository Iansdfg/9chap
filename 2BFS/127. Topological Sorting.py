"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
from collections import deque
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        node_indegree = self.get_indegree(graph)
        starts = [key for key in node_indegree if node_indegree[key] == 0]
        queue = deque(starts)
        order = []
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for neighbor in curr.neighbors:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order
                
     

    def get_indegree(self, graph):
        node_indegree = {x:0 for x in graph }
        for node in graph:
            for neighbor in node.neighbors:
                node_indegree[neighbor] += 1 
        return node_indegree

