from collections import deque
class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: a list of lists of string
             we will sort your return value in output
    """
    def find_ladders(self, start, end, dict):
        #write your code here
        queue = deque([end])
        dict.add(start)
        dict.add(end)


        word2step = {
            end:0
        }
        step = 1
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for next_word in self.find_next(curr, dict):
                    if next_word in word2step:
                        continue
                    word2step[next_word] = step
                    queue.append(next_word)
            step += 1 

        paths = []
        self.dfs(start, end, dict, word2step, [start], paths)
        return paths

    
    def dfs(self, curr, target, dict, word2step, path, paths):
        if curr == target:
            paths.append(path[:])
            return

        for next_word in self.find_next(curr, dict):
            if word2step[curr] - 1 !=  word2step[next_word]:
                continue
            path.append(next_word)
            self.dfs(next_word, target, dict, word2step, path, paths)
            path.pop()


    def find_next(self, word, dict):
        new_words = []
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + char +word[i+1:]
                if new_word != word and new_word in dict:
                    new_words.append(new_word)
        return new_words





