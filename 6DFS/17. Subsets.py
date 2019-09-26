class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        ans = []
        self.findsub(nums,0, [], ans)
        return ans
        
    def findsub(self, nums,level, path, ans):
        if len(nums) == level:
            ans.append(path[:])
            return ans
        path.append(nums[level])
        self.findsub(nums,level+1, path, ans)
        path.pop()
        self.findsub(nums,level+1, path, ans)
    
