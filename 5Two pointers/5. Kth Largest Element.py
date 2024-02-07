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
        # 判断条件是看 k 在 start-right OR pivot OR left-end 中 
        # [start:right][pivot][left:end]
        # 而不是比较 k 和 mid 的关系
        # use k <= right or k >= left because if k == right/left, k is not pivit, 
        # and we want to partition to right/left
        if k <= right:
            return self.quick_select(k , nums, start, right)
        elif k >= left:
            return self.quick_select(k , nums, left, end)
        else:
            return pivot


class Solution(object):
    def findKthLargest(self, nums, k):
        # write your code here
        n = len(nums)
        k = n - k
        return self.partition(nums, 0, n - 1, k)

    def partition(self, nums, start, end, k):
        left, right = start, end
        pivit = nums[left]
        while left <= right:
            while left <= right and nums[left] < pivit:
                left += 1 
            while left <= right and nums[right] > pivit:
                right -= 1 
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1 
                right -= 1 

        # after partition: OOOR P LXXX
        
        if k <= right:
            return self.partition(nums, start, right, k)
        if k >= left:
            return self.partition(nums, left, end, k)

        return nums[k] # find the k and its the pivit number. Return it

            

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # 0 th large == 6th small
        # 1 th large == 5th small 
        # k th large == n-k th small
        n_k = len(nums) - k
        res = self.quick_select(nums, n_k, 0, len(nums)-1)
        return res

    def quick_select(self, nums, k, start, end):
        # find kth small
        l, r = start, end
        pivit = nums[(l + r)//2]

        while l <= r:
            while l <= r and nums[l] < pivit:
                l += 1 
            while l <= r and nums[r] > pivit:
                r -= 1  
            if l <= r: 
                # we want to use <= instead of <, want to devide this in 3 parts:
                # [:l][k][r:]
                nums[l], nums[r] = nums[r], nums[l]
                l += 1 
                r -= 1 
        
        # [:l]< pivit
        # [k] == pivit
        # [:r] > pivit
        if k <= r: # when pivit < kth
            self.quick_select(nums, k, start, r)
        if k >= l: # when pivit > kth
            self.quick_select(nums, k, l, end)
        return nums[k] # when pivit == kth
                    

        



        


        

