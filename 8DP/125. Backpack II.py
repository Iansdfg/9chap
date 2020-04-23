class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A) 
        # dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        dp = [0 for _ in range(m + 1)]
        
        for row in range(1, n + 1):
            
            new_dp =  [0 for _ in range(m + 1)]
            
            for col in range(1, m + 1):
                if  A[row - 1] > col:
                    new_dp[col] = dp[col]
                    continue
                take = dp[col - A[row - 1]] + V[row - 1]
                no_take = dp[col]
                new_dp[col] = max(take, no_take)
                
            dp = new_dp
            
        return dp[-1]
