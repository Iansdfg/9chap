class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1 
        visited = set()

        while left <= right:
            if nums[left] not in visited:
                visited.add(nums[left])
                left += 1 
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1 
        return left 
