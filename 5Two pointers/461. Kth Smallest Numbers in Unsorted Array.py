vclass Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if not nums or k<1 or k>len(nums):
            return None
        return self.quick_select(k-1, nums, 0, len(nums)-1)

    def quick_select(self, k, nums, start, end):
        if start>=end:
            return nums[k]
            
        left, right = start, end
        pivot = nums[(start + end)//2]
        while left<=right:
            while left <= right and nums[left]<pivot:
                left+=1
            while left <= right and nums[right]>pivot:
                right-=1
            if left<=right:
                nums[right], nums[left] = nums[left], nums[right] 
                left+=1
                right-=1
            
        if k <= right:
            return self.quick_select(k, nums, start, right)
        elif k >= left:
            return self.quick_select(k, nums, left, end)
        return nums[k]
                
  
