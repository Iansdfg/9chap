from collections import deque

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = deque([start])
        visited = set([start])
        count = 0
        
        while queue:
            count += 1
            # think word ladder as a trie, distance is height from root to 
            # the leaf. So layering to check height.
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return count
                
                for new_word in self.get_next_words(word):
                    if new_word in visited or new_word not in dict:
                        continue
                    queue.append(new_word)
                    visited.add(new_word)
        return 0
        
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                new_word = word[:i] + char + word[i+1:]
                words.append(new_word)
        return words
        
    
