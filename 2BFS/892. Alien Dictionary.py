from typing import (
    List,
)
from heapq import heappush, heappop, heapify

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Write your code here
        graph = self.build_graph(words)
        if not graph:
            return ''
        print("graph, ", graph)
        return self.sort(words, graph)


    def build_graph(self, words):
        char_to_next = {}
        for word in words:
            for char in word:
                if char not in char_to_next:
                    char_to_next[char] = set()
        
        for nth_word in range(len(words)-1):
            word, next_word = words[nth_word], words[nth_word+1]
            for nth_char in range(min(len(word), len(next_word))):
                if word[nth_char] != next_word[nth_char]:
                    char_to_next[word[nth_char]].add(next_word[nth_char])
                    #have to stop the look when find next char
                    break 
                
                if nth_char == min(len(word), len(next_word))-1:
                    if len(word) > len(next_word):
                        return None
        return char_to_next     

    def sort(self, words, graph):
        #graph: char_to_next
        char_indegree = {}
        for char in graph:
            char_indegree[char] = 0
        
        for char in graph:
            for next_char in graph[char]:
                char_indegree[next_char] += 1 

        queue = []
        for char in char_indegree:
            if char_indegree[char] == 0:
                queue.append(char)
        heapify(queue)

        order = ''
        while queue:
            curr_char = heappop(queue)
            order += curr_char

            for next_char in graph[curr_char]:
                char_indegree[next_char] -= 1 
                if char_indegree[next_char] == 0:
                    heappush(queue, next_char)
        if len(order) == len(graph):
            return order
        return ''
        
        
        


