class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s, word_set):
        # write your code here
        if not word_set:
            return s == ''
        memo = {x:None for x in range(len(s)+1)}
        memo[0] = True
        self.memorize(s, word_set, memo)
        return memo[len(s)] == True

    def memorize(self, s, word_set, memo):
        max_len = max(len(word) for word in word_set)
        for i in range(len(s) + 1):
            for j in range(max(0, i - max_len), i):
                if memo[j] and s[j:i] in word_set:
                    memo[i] = True 


