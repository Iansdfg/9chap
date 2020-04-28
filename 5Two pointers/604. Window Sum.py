class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        results = []
        if len(nums) == 0 or k == 0:
            return results 
        len_res = len(nums) - k + 1
        res = [0]*len_res
        for i in range(k):
            res[0] += nums[i]    
        for i in range(1, len_res):
            res[i] = res[i-1] - nums[i - 1] + nums[i + k - 1]
        return res 
           
