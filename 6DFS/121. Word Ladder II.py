from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        dict.add(start)
        dict.add(end)
        distance = {}
        
        self.bfs(end, start, distance, dict)
        results = []
        self.dfs(start, end, distance, dict, [start], results)
        return results
        
    def bfs(self, start, end, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word]+1
                    queue.append(next_word)
                    
    def get_next(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words
    
    def dfs(self, curr, target, distance, dict, path, results):
        if curr == target:
            results.append(list(path))
            return
        
        for word in self.get_next(curr, dict):
            if distance[word]!=distance[curr]-1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()
      
