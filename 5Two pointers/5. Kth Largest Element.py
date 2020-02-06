class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        start, end = 0, len(nums) - 1 
        return self.helper(n-1, nums, start, end)
        
    def helper(self, n, nums, start, end):
        if start == end:
            return nums[start]
        
        left, right = start, end
        
        pivot = nums[ (left + right) // 2 ]
        
        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1 
                
            while left <= right and nums[right] < pivot:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 
                
        if n <= right:
            return self.helper(n, nums, start, right)
        elif n >= left:
            return self.helper(n, nums, left, end)
        else:
            return nums[n]
        
        
