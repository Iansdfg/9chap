class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longest_increasing_subsequence(self, nums):
        # write your code here
        if not nums:
            return 0
        dp =[1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i):
                # print(i, j, nums[i], nums[j])
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
