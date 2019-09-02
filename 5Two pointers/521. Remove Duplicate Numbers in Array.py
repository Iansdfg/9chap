class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if len(nums) == 0: return 0 
        nums.sort()

        res = 1
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[res] = nums[i]
                res+=1
        return res
                
    class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        visited = set()
        left,right = 0,0
        while right<len(nums):
            if nums[right] not in visited:
                visited.add(nums[right])
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            right+=1
        return left
 
