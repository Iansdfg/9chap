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
        node_indegree_dic = self.get_node_indegree(graph)
        
        start = [n for n in node_indegree_dic if node_indegree_dic[n] == 0]
        order = []
        queue = collections.deque(start)
        while queue:
            curr_node = queue.popleft()
            order.append(curr_node)
            for neighbor in curr_node.neighbors:
                node_indegree_dic[neighbor] -=1
                if node_indegree_dic[neighbor] == 0:
                    queue.append(neighbor)
        return order
                
    def get_node_indegree(self,graph):
        indegree_dic ={x:0 for x in graph}
        
        for node in graph:
            for neighbor in node.neighbors:
                indegree_dic[neighbor]+=1
                
        return indegree_dic
