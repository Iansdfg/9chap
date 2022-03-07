class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def find_min(self, nums):
        # write your code here
        if not nums:
            return -1
        start, end = 0, len(nums) - 1 
        while start + 1 < end:
            mid = (start + end) // 2 
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            else:
                #why end -= 1 instead of start +=1:
                #if arrary is not rotated, start += 1 
                #will cut the min number, thus cannot 
                #find the right answer. 
                end -= 1 
        return min(nums[start], nums[end])
