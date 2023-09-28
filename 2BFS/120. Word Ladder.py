####注意放进visited的时间点：pop out vs create （选择create的时候放入， 这样不用在loop里判断是否在queue里）


from typing import (
    Set,
)

from collections import deque
APLHA = "abcdefghijklmnopqrstuvwxyz"

class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        # write your code here
        queue = deque([start])
        res = 1
        visited = set([start])
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                for i in range(len(curr_word)):
                    for alp in APLHA:
                        new_word = curr_word[:i] + alp + curr_word[i+1:]
                        if new_word == end:
                            return res+1
                        if new_word in visited:
                            continue
                        if new_word in dict:
                            queue.append(new_word)
                            visited.add(new_word)
            res += 1 
        return 0
                        


