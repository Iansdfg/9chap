###### O(n^2) ######

from typing import (
    List,
)

class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def max_envelopes(self, envelopes: List[List[int]]) -> int:
        # write your code here
        dp = [1 for i in range(len(envelopes))]
        envelopes.sort()

        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1 

        return max(dp)
        
