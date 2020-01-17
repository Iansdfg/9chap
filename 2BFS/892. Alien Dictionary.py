from heapq import heapify, heappush, heappop
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.built_graph(words)
    
        return self.topological_sort(graph)

        
    def built_graph(self, words):
        char_to_nexts = {}
        
        for word_pos in range(len(words)):
            for char_pos in range(len(words[word_pos])):
                char = words[word_pos][char_pos]
                # print(char)
                if char not in char_to_nexts:
                    char_to_nexts[char] = set()
                    
        n = len(words)
        for word_pos in range(n - 1):
            for char_pos in range(min(len(words[word_pos]), len(words[word_pos+1]))):
                print(words[word_pos][char_pos], words[word_pos+1][char_pos])
                if words[word_pos][char_pos] != words[word_pos+1][char_pos]:
                    char_to_nexts[words[word_pos][char_pos]].add(words[word_pos+1][char_pos])
                    break
                
        return char_to_nexts
        
    
    def topological_sort(self, graph):
        print('graph: ', graph)
        indegree = {node:0 for node in graph}
        
        for node in graph:
            for neighber in graph[node]:
                indegree[neighber] += 1 
                
        print(indegree)
        
        queue = [node for node in indegree if indegree[node] == 0]
        heapify(queue)
        print(queue)
        
        order = ''
        while queue:
            curr = heappop(queue)
            order += curr 
            for neighber in graph[curr]:
                indegree[neighber] -= 1
                if indegree[neighber] == 0:
                    heappush(queue, neighber)
                
        
        return order if len(order) == len(graph) else ''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                    
                
