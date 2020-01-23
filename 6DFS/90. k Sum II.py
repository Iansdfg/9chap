class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        A.sort()
        results = []
        self.dfs(A, k, target, 0, [], results)
        return results
        
    def dfs(self, A, k, target, index, path, results):
        if sum(path) > target or len(path) > k:
            return
        
        if sum(path) == target and len(path) == k:
            results.append(path[:])
            return
        
        for i in range(index, len(A)):
            path.append(A[i])
            self.dfs(A, k, target, i+1, path, results)
            path.pop()
        
