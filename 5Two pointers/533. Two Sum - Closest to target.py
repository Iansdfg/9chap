class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        min_val = float('inf')
        start, end = 0, len(nums) - 1 
        while start < end:
            value = nums[start] + nums[end]
            if abs(value - target) < min_val:
                    min_val = abs(value - target)
            if value > target:
                end -= 1 
            elif value < target:
                start += 1 
            else:
                return 0 
        return min_val
            
