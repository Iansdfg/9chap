class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums, target):
        # write your code here
        nums.sort()
        cnt = 0
        start, end = 0, len(nums) - 1 
        while start < end:
            value = nums[start] + nums[end]
            if value <= target:
                cnt += end - start
                start += 1 
            else:
                end -= 1 
        return cnt
