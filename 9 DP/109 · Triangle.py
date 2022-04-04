class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimum_total(self, triangle):
        # write your code here
        n = len(triangle)
        dp = [[0] * (i + 1) for i in range(n) ]

        dp[0][0] = triangle[0][0]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + triangle[i][0]
            dp[i][i] = dp[i-1][i-1] + triangle[i][i]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[-1])

