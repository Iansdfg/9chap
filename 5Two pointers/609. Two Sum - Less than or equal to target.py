class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        l, r = 0, len(nums)-1
        res = 0
        nums.sort()
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum > target:
                r -= 1
            else:
                res += r - l
                l += 1
        return res
        
        
