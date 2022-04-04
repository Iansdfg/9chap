class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if not s:
            return True
        if not dict:
            return False 
        len_s = len(s)
        dp = [0] * (len_s + 1)
        dp[0] = 1 
        max_len = max([len(w) for w in dict])
        for i in range(len_s+1):
            for j in range(max(0, i - max_len), i):
                if not dp[j]:
                    continue
                
                if s[j:i] in dict:
                    dp[i] = 1
                    break 
                    
        return bool(dp[-1])
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        n = len(s)
        dp = [0]*(n + 1)
        dp[0] = 1
        
        for i in range(n + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                if s[j:i] in dict:
                    dp[i] = 1 
                    break 
                
        return bool(dp[-1])

    
    
    
class Solution:
    """
    @param s: A string
    @param word_set: A dictionary of words dict
    @return: A boolean
    """
    def word_break(self, s, word_set):
        # write your code here
        res = self.dfs(s, word_set, 0)
        return res 


    def dfs(self, s, word_set, index):
        #return if s[:index], s[index:] is valid 
        if index == len(s):
            return True 

        #iterate all [:i] [i:]
        for i in range(index, len(s)):
            if s[index:i+1] in word_set and self.dfs(s, word_set, i + 1):
                return True 

        return False 
        



