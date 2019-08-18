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
        res = 1
        
        for pos in range(1, len(nums)):
            if nums[pos]!=nums[pos-1]:
                nums[res]=nums[pos]
                res+=1
        return res
            
