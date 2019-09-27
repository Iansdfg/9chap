class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if not s:
            return[[]]
            
        ans = []
        self.dfs(s, [], ans)
        return ans
        
    def dfs(self, s, path, ans):
        if s=='':
            ans.append(path[:])
            return ans
            
        for i in (1,2):
            if len(s)>=i:
                path.append(s[:i])
                self.dfs(s[i:], path, ans)
                path.pop()
        
        
