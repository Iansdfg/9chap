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
        order = []
        node_to_indegree = self.get_indegree(graph)
        start_nodes = [
            key for key in node_to_indegree if node_to_indegree[key] == 0]
        queue = deque(start_nodes)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] -= 1 
                if node_to_indegree[neighbor] == 0:
                    queue.append(neighbor)
        return order
        

    
    def get_indegree(self, graph):
        node_to_indegree = {x: 0 for x in graph}

        for node in graph:
            for neighbor in node.neighbors:
                node_to_indegree[neighbor] += 1
                
        return node_to_indegree
