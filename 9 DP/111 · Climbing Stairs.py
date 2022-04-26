class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climb_stairs(self, n):
        # write your code here
        if n < 3:
            return n
        dp = [0 for _ in range(n + 1)]

        for i in range(n + 1):
            if i < 3:
                dp[i] = i
            else:
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
