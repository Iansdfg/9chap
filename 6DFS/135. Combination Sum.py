class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results
        
    def dfs(self, candidates, target, index, path, results):
        if sum(path) > target:
            return
        
        if sum(path) == target:
            results.append(path[:])
            
        for i in range(index, len(candidates)):
            if i>index and candidates[i] == candidates[i-1]:
                continue
            path.append(candidates[i])
            self.dfs(candidates, target, i, path, results)
            path.pop()
            
