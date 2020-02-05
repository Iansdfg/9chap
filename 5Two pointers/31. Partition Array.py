class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        start, end = 0, len(nums)-1 
        
        while start <= end:
            while start <= end and nums[start] < k:
                start += 1 
                
            while start <= end and nums[end] >= k:
                end -= 1 
                
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1 
                end -= 1 
                
        return start
            
