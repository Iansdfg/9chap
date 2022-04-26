class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climb_stairs2(self, n):
        # write your code here
        if n < 2:
            return 1 
        if n == 2:
            return 2 
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1 
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[-1]
