class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        left, mid, right = 0, 0, len(nums) - 1
        while mid <= right:
            if nums[mid] < low:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid += 1 
                left += 1 
            elif low <= nums[mid] <= high:
                mid += 1 
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1 
        return nums
