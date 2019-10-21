class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        left, right = 0, len(nums)-1
        i = 0
        while i<=right:
            if nums[i]<low:
                nums[i], nums[left] = nums[left], nums[i]
                left+=1
                i += 1
            elif low <= nums[i] <= high:
                i += 1 
            elif nums[i]>high:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
                
