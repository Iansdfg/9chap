import math
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        results = []
        self.dfs(n, 2, [], results)
        return results
        
        
    def dfs(self, n, index, path, results):
        if path:
            path.append(n)
            results.append(path[:])
            path.pop()
            
        for i in range(index, int(math.sqrt(n)) + 1):
            if n % i:
                continue
            path.append(i)
            self.dfs(n//i, i, path, results)
            path.pop()
            

