class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end)//2
            print(mid)
            if nums[mid] > nums[mid - 1]:
                start = mid 
            elif nums[mid] < nums[mid - 1]:
                end = mid 
        
        return max(nums[start], nums[end])
