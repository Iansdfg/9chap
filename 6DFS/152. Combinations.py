class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        combinations = []
        self.dfs(candidates, target, 0, [], combinations)
        return combinations
        
    def dfs(self, candidates, target, index, combination, combinations):
        if sum(combination) > target:
            return
        
        if sum(combination) == target:
            combinations.append(combination[:])
            return
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i-1]:
                continue
            combination.append(candidates[i])
            self.dfs(candidates, target, i , combination, combinations)
            combination.pop()
        
        
        
