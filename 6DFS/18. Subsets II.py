class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums:
            return [[]]
        nums.sort()
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans
        
        
    def dfs(self, nums, index, path, ans):
        ans.append(path[:])
        for i in range(index, len(nums)):
            if i>0 and nums[i] == nums[i-1] and i!=index:
                continue
            path.append(nums[i])
            self.dfs(nums, i+1, path, ans)
            path.pop()
