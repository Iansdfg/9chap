from heapq import heappush, heappop, heapify

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.built_graph(words)
        order = self.topological_sort(graph)
        return order
        
    def built_graph(self, words):
        char_to_next = {}
        
        # initiate graph
        for word in words:
            for char in word:
                if char not in char_to_next:
                    char_to_next[char] = set()
                    
        n = len(words)
        for pos_word in range(n-1):
            for pos_char in range(min(len(words[pos_word]), len(words[pos_word + 1]))):
                # to avoid same prefix, if not same, 
                if words[pos_word][pos_char] != words[pos_word+1][pos_char]:
                    char_to_next[words[pos_word][pos_char]].add(words[pos_word+1][pos_char])
                    break
                
        return char_to_next
        
    def topological_sort(self, graph):
        indegree = {node:0 for node in graph}
        
        for node in graph:
            for neighber in graph[node]:
                indegree[neighber] += 1
                
        queue = [node for node in graph if indegree[node] == 0 ]
        heapify(queue)
        
        order = ''
        while queue:
            node = heappop(queue)
            order += node
            for neighber in graph[node]:
                indegree[neighber] -= 1 
                if indegree[neighber] == 0:
                    heappush(queue, neighber)
                    
        return order if len(order) == len(graph) else ''
            
        
        
              
