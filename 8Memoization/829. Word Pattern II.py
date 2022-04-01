class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def word_pattern_match(self, pattern, string):
        # write your code here
        return self.dfs(pattern, string, set(), dict())


    def dfs(self, pattern, string, visited, char2word):
        if not pattern:
            return string==''

        char = pattern[0]
        if char in char2word:
            word = char2word[char]
            if not string.startswith(word):
                return False
            return self.dfs(pattern[1:], string[len(word):], visited, char2word)
            

        for i in range(len(string)):
            word = string[:i+1]

            if word in visited:
                continue

            visited.add(word)
            char2word[char] = word
            if self.dfs(pattern[1:], string[i+1:], visited, char2word):
                return True
            del char2word[char]
            visited.remove(word)

        return False 
