class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1 
        res = float('inf')
        
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum > target:
                res = min(res, abs(two_sum - target))
                right -= 1 
            elif two_sum < target:
                res = min(res, abs(two_sum - target))
                left += 1 
            elif two_sum == target:
                return 0
                
        return res 
                
            
