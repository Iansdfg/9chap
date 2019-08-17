class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums)-1
        pivit = nums[0]
        
        if pivit<nums[-1]:
            return pivit
        
        while start+1<end:
            mid = (start+end)//2
    
            if nums[mid]<pivit:
                end = mid
            elif nums[mid]>pivit:
                start = mid
            else:
                start = mid
                
        print(nums[start],nums[end])
        
        return nums[start] if nums[start]<nums[end] else nums[end]
