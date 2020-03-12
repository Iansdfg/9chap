from collections import deque

class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        # write your code here
        queue = deque([s])
        visited = set([s])
        
        min_len = len(s)
        while queue:
            curr = queue.popleft()
        
            for sub in dict:
                found = curr.find(sub)
                min_len = min(min_len, len(curr))
                while found != -1:
                    new_s = curr[:found] + curr[found + len(sub):]
                    if new_s not in visited:
                        visited.add(new_s)
                        queue.append(new_s)
                        
                    found = curr.find(sub, found + 1)
                    
        return min_len
