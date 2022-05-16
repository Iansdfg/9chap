class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longest_increasing_subsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    # why use max(dp[j] + 1, dp[i])
                    # counter eg: [9,3,6,2,7]
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
