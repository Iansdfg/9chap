class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        count = 0
        left, right = 0, len(nums)-1 
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum <= target:
                count += right - left
                left += 1 
                
            elif two_sum > target:
                right -= 1 
        
        return count
