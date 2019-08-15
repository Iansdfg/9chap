class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        if nums == [] or not target: return -1
        l,r = 0, len(nums)-1
        
        while l+1<r:
            m = (l+r)//2
            
            if nums[m] > target:
                r = m 
            elif nums[m] < target:
                l = m 
            else:
                l = m 
            
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l
        return -1
