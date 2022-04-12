class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s, word_set):
        # write your code here

        dp = [False for i in range(len(s) + 1)]
        dp[0] = True 

        max_len = 0
        for word in word_set:
            max_len = max(max_len, len(word))
            
        for i in range(len(s) + 1):
            for j in range(max(i - max_len, 0), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True 

        return dp[-1]
