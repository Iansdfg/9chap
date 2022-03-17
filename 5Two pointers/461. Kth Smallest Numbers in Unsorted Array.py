class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kth_smallest(self, k, nums):
        # write your code here
        return self.quck_select(k - 1, nums, 0, len(nums) - 1)

    def quck_select(self, k, nums, start, end):
        left, right = start, end

        pivot = nums[(left + right) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1 
            while left <= right and nums[right] > pivot:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        print(left, right, k)

        if right >= k: 
            #>=: the partitioned part is not sorted. 
            #when k == right right might not be the target
            return self.quck_select(k, nums, start, right)
        elif left <= k:
            return self.quck_select(k, nums, left, end);
        else:#when right < key < left
            return nums[k];
