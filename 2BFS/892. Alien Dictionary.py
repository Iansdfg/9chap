from heapq import heapify, heappop, heappush
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.built_graph(words)
        print(graph)
        return self.topological_sort(graph)
        
    def built_graph(self, words):
        
        char_to_next = {}
        
        for word in words:
            for char in word:
                if char not in char_to_next:
                    char_to_next[char] = set()
                    
        n = len(words)
        for word_pos in range(n - 1):
            for char_pos in range(min(len(words[word_pos]), len(words[word_pos + 1]))):
                if words[word_pos][char_pos] != words[word_pos+1][char_pos]:
                    char_to_next[words[word_pos][char_pos]].add(words[word_pos+1][char_pos])
                    break
        
        return char_to_next
        
        
    def topological_sort(self, graph):
        indegree = {node:0 for node in graph}
        
        for node in graph:
            for neighber in graph[node]:
                indegree[neighber] += 1
        
        queue = [node for node in indegree if indegree[node] == 0]
        heapify(queue)
        
        order = ''
        while queue:
            curr = heappop(queue)
            order += curr
            for neighber in graph[curr]:
                indegree[neighber] -= 1
                if indegree[neighber] == 0:
                    heappush(queue, neighber)
        
        return order if len(order) == len(graph) else ''
        
