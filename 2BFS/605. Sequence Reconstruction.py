from collections import deque

class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        # write your code here
            
        graph = self.build_graph(seqs)
        order = self.check_unique(graph)
        return order == org
        
        
    def build_graph(self, seqs):
        node_to_next = {}
        
        for seq in seqs:
            for node in seq:
                if node not in node_to_next:
                    node_to_next[node] = set()
                    
        for seq in seqs:
            for node_pos in range(len(seq)-1):
                node_to_next[seq[node_pos]].add(seq[node_pos+1])
                
        return node_to_next
        
        
    def check_unique(self, graph):
        indegree = {node:0 for node in graph}
        
        for node in graph:
            for neighber in graph[node]:
                indegree[neighber] += 1 
                
        queue = deque([])
        for node in indegree:
            if indegree[node] == 0:
                queue.append(node)
                
        order = []
        while queue:
            if len(queue) > 1:
                return None
            curr = queue.popleft()
            order.append(curr)
            for neighber in graph[curr]:
                indegree[neighber] -= 1 
                if indegree[neighber] == 0:
                    queue.append(neighber)
            
        return order if len(order) == len(graph) else None 
