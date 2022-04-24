APLHA = "abcdefghijklmnopqrstuvwxyz"

from collections import deque
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start, end, dict):
        # write your code here
        queue = deque([start])
        visited = set([start])
        step = 1

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for i in range(len(curr)):
                    for char in APLHA:
                        new_word = curr[:i] + char + curr[i+1:]
                        if new_word == end:
                            return step + 1 
                        if new_word in dict:
                            if new_word in visited:
                                continue
                            queue.append(new_word)
                            visited.add(new_word)
            step += 1 

        return -1
    

        

                        

