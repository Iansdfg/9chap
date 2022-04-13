class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kth_largest_element(self, k, nums):
        # write your code here
        # right bondary is len(nums) - 1 b/c we need to use num[right] to partition
        # the Kth largest the index is k - 1 
        return self.helper(k - 1, nums, 0, len(nums)-1)


    def helper(self, k, nums, start, end):
        if start == end:
                return nums[start]
            
        left, right = start, end 

        mid = (left + right) // 2
        pivot = nums[mid]

        while left <= right:
            while left <= right and nums[left] > pivot:
                left += 1 
            while left <= right and nums[right] < pivot:
                right -= 1 

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 

        # 判断条件是看 k 在 start-right, right-left, left-end 中 
        # 而不是比较 k 和 mid 的关系
        # use k <= right/left because if k == right/left we want to partition with right/left
        if k <= right:
            return self.helper(k, nums, start, right)
        elif k >= left:
            return self.helper(k, nums, left, end)
        else:
            return nums[k]

