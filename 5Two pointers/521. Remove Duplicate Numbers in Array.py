class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0 
            
        nums.sort()
        slow = 0
        
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1 
                nums[slow] = nums[fast]
                
        return slow + 1 
                

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        visited = set()
        left, right = 0, len(nums) - 1 
        while left <= right:
            if nums[left] not in visited:
                visited.add(nums[left])
                left += 1 
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1 
        return left


                
