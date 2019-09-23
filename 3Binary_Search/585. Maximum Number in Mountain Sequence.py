class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        
        if nums == []: return -1
        start, end = 0, len(nums)-1    
        while start+1<end:
            m = (start+end)//2
            if nums[m]<nums[m+1]:
                start = m 
            elif nums[m]>nums[m+1]:
                end = m        
        return max(nums[start],nums[end])
