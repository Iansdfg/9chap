class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def win_sum(self, nums, k):
        # write your code here
        if not nums:
            return []
        summ = 0 
        for i in range(k):
            summ += nums[i]

        res = [summ]
        for i in range(k, len(nums)):
            summ = summ + nums[i] - nums[i-k]
            res.append(summ)
        return res 




