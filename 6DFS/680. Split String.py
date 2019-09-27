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
        
        path.append(s[:1])
        self.dfs(s[1:], path, ans)
        path.pop()
        
        if len(s)>=2:
            path.append(s[:2])
            self.dfs(s[2:], path, ans)
            path.pop()
        
