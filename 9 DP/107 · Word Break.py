class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s, word_set):
        # write your code here
        if not s:
            return True
        if not word_set:
            return False 
        dp = [False for _ in range(len(s)+1)]

        max_len = max([len(word) for word in word_set])
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(max(i - max_len, 0), i):
                if not dp[j]:
                    continue
                if s[j:i] in word_set:
                    
                    dp[i] = True
                    break 
        return dp[-1]
