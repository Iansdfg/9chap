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
        return self.quick_select(k - 1, nums, 0, len(nums) - 1)


    def quick_select(self, k, nums, start, end):
        # if start == end:
        #     return nums[start]

        left, right = start, end

        pivot = nums[(left + right)//2]

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
        #[start:right][pivot][left:end]
        # 而不是比较 k 和 mid 的关系
        # use k <= right/left because if k == right/left we want to partition with right/left
        if k <= right:
            return self.quick_select(k , nums, start, right)
        elif k >= left:
            return self.quick_select(k , nums, left, end)
        else:
            return pivot

        

