class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        res = 0
        left, right = 0, len(nums) - 1 
        while left < right:

            if nums[right] + nums[left] > target:
                right -= 1 
            elif nums[right] + nums[left] < target:
                left += 1 
            else:
                res += 1 
                left += 1 
                right -= 1 
                
            while left < right and left > 0 and nums[left] == nums[left - 1]:
                left += 1 
            while left < right and right < len(nums) - 1 and nums[right] == nums[right + 1]:
                right -= 1 
            
        return res
