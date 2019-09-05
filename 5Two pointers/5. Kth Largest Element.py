class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n<1 or n>len(nums):
            return None
        return self.quick_select(len(nums)-n, nums, 0, len(nums)-1)
    
    def quick_select(self, n, nums, start, end):
        if start == end:
            return nums[n]
            
        left, right = start, end
        pivot = nums[(start + end) // 2]
        
        while left<=right:
            while left <= right and nums[left]<pivot:
                left+=1
            while left <= right and nums[right]>pivot:
                right-=1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        
                
        if n<=right:
            return self.quick_select(n, nums, start, right)
        elif n>=left:
            return self.quick_select(n, nums, left, end)
        
        return nums[n]
