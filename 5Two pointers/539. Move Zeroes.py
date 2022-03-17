class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def move_zeroes(self, nums):
        # write your code here
        left, right = 0, 0 
        while right < len(nums):
            if nums[right] != 0:
                nums[left] = nums[right]
                left += 1 
            right += 1

        while left < len(nums):
            if nums[left] != 0: 
                nums[left] = 0
            left += 1


