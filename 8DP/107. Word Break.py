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
        n = len(s)
        # dp[j]若為True 表示該數列可以透過dictionary組出0~j的字串
        dp = [0] * (n + 1) 
        dp[0] = 1 
        max_len = max([len(word) for word in dict])
        for i in range(1, n + 1):
            for j in range(max(i-max_len, 0), i):
                if not dp[j]:
                    continue
                if s[j:i] in dict:
                    dp[i] = 1
                    break
        return bool(dp[-1])
                    
            
