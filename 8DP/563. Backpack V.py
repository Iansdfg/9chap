class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        num_len = len(nums)
        dp = [[0 for _ in range(target + 1)] for _ in range(num_len + 1)]
        dp[0][0] = 1 
        for row in range(1, num_len + 1):
            for col in range(target + 1):
                dp[row][col] = dp[row - 1][col]
                
                if col < nums[row - 1]:
                    continue
                dp[row][col] += dp[row - 1][col - nums[row - 1]]
        print(dp)
        return dp[-1][-1]
        
