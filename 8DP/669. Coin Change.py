class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            cases = []
            for coin in coins:
                if i - coin < 0:
                    cases.append(float('inf'))
                else:
                    cases.append(dp[i - coin] + 1)
            dp[i] = min(cases)
        return -1 if dp[-1] == float('inf') else dp[-1]
