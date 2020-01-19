class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations
        
        
    def dfs(self, nums, index, combination, combinations):
        combinations.append(combination[:])
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()
        
