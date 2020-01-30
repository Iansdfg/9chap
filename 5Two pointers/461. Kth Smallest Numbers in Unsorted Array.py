class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if k > len(nums):
            return -1 
            
        start, end = 0, len(nums)-1
        return self.quick_select(k - 1, nums, start, end)
        
        
    def quick_select( self, k, nums, start, end):
        
        if start == end:
            return nums[start]
    
        left, right = start, end
        
        pivot = nums[(left + right)//2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[right], nums[left] = nums[left], nums[right]
                left +=1 
                right -= 1
                
            
        if k <= right:
            return self.quick_select(k , nums, start, right)
        elif left <= k:
            return self.quick_select(k , nums, left, end)
        else:
            return nums[k]
                

            
