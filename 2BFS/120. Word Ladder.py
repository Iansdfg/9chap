
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if start == end: return 0
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        step = 0
        while queue:
            step+=1
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == end:
                    return step
                for i in range(len(curr_word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = curr_word[:i] + char + curr_word[i+1:]
                        if new_word in dict and new_word not in visited:
                            queue.append(new_word)
                            visited.add(new_word)
        return 0
