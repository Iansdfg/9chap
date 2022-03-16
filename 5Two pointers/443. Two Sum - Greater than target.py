class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def two_sum2(self, nums, target):
        # write your code here
        nums.sort()
        cnt = 0
        start, end = 0, len(nums) - 1 
        while start < end:
            value = nums[start] + nums[end]
            if value > target:
                cnt += end - start
                end -= 1 
            else:
                start += 1 
        return cnt
        
