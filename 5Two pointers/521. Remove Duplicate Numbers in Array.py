class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        nums.sort()
        slow = 1 
        for fast in range(1, len(nums)):
            if nums[fast - 1] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1 
                
        return slow
                
            
            
