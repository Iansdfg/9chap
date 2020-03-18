class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        results = []
        self.dfs(s, [], results)
        return results
        
    def dfs(self, s, path, results):
        if len(s) == 0:
            results.append(path[:])
            return 
        
        for i in [1, 2]:
            if i <= len(s):
                path.append(s[:i])
                self.dfs(s[i:], path, results)
                path.pop()
            
        
