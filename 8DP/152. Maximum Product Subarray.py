class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        max_dp, min_dp = [0]*n, [0]*n
        max_dp[0], min_dp[0] = nums[0], nums[0]
        res = nums[0]
        for i in range(1, n):
            max_dp[i] = max(max(nums[i] * max_dp[i-1], nums[i] * min_dp[i-1]), nums[i])
            min_dp[i] = min(min(nums[i] * max_dp[i-1], nums[i] * min_dp[i-1]), nums[i])
            res = max(res,max_dp[i])
        return res
            
        
