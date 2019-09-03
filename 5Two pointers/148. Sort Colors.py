###three-pointer
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if not nums:return nums
        
        left, right = 0, len(nums)-1
        
        i = 0
        while i<=right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i+=1
                left+=1
            elif nums[i] == 1:
                i+=1
            elif nums[i] == 2:
                nums[right], nums[i] = nums[i], nums[right]
                right-=1
            
###two-pointer
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        one_start = self.sort_by_target(nums, 0, 0)
        # print(one_start)
        two_start = self.sort_by_target(nums, 1, one_start)
        
        return nums

    def sort_by_target(self, nums, target,start):
        left, right = start, len(nums)-1
        
        while left<=right:
            while left<=right and nums[left]<= target:
                left+=1
                
            while left<=right and nums[right]> target:
                right-=1
                
            if  left<=right:
                nums[left],nums[right] = nums[right], nums[left]
                left+=1
                right-=1
                
        return left
        
