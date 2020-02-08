class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        write your code here
        if len(nums) < 2 :
            return nums
            
        slow = 0
        while nums[slow]:
            slow += 1 
            if slow >= len(nums):
                return nums
         
        fast = slow + 1 
        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1 
            elif nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow += 1 
                
        return nums
            
