class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        start, end = 0, len(nums) - 1 
        return self.helper(k - 1 , nums, start, end)
        
        
    def helper(self, k, nums, start, end):
        if start == end:
            return nums[start]
            
            
        left, right = start, end
    
        pivot =nums[(left + right)//2] 
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
                
        if k <= right:
            return self.helper(k, nums, start, right)
            
        elif k >= left :
            return self.helper(k, nums, left, end)
            
        return nums[k] 
            
            
        
