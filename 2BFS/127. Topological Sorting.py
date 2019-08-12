"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        node_in_degree = self.get_in_degress(graph)
        order = []
        start_nodes = [n for n in graph if node_in_degree[n]==0 ]
        queue = collections.deque(start_nodes)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in node.neighbors:
                node_in_degree[neighbor] -= 1
                if node_in_degree[neighbor]==0:
                    queue.append(neighbor)
        return order
        
    def get_in_degress(self,graph):
        node_indegree = {x: 0 for x in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                node_indegree[neighbor]+=1
                
        return node_indegree
        
        
    
