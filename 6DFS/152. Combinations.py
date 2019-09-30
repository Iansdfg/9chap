class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results = []
        self.dfs(n, k, 1, [], results)
        return results
        
    def dfs(self, n, k, index, path, results):
        if len(path) == k:
            results.append(path[:])
            return
        
        for i in range(index, n+1):
            if len(path)>0 and i <= path[-1]:
                continue
            path.append(i)
            self.dfs(n, k, index+1, path, results)
            path.pop()
