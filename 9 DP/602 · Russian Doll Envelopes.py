class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def max_envelopes(self, envelopes):
        # write your code here
        if not envelopes:
            return 0
        envelopes.sort()
        dp = [1 for i in range(len(envelopes))]
        for i in range(len(envelopes)):
            for j in range(i):
                if self.is_valid(envelopes[i], envelopes[j]):
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    def is_valid(self, e1, e2):
        if e1[0] > e2[0] and e1[1] > e2[1]:
            return True 
        return False 
