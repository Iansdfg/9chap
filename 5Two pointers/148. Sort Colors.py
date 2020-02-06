class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        left, mid, right = 0, 0, len(nums) - 1 
        
        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                mid += 1 
                left += 1 
                
            elif nums[mid] == 1:
                mid += 1 
                
            elif nums[mid] == 2:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1 
