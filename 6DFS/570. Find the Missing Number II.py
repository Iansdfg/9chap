class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, s):
        # write your code here
        results = []
        self.dfs(n, s, [], results)
        
        for i in range(1, n+1):
            if str(i) not in results[0]:
                return i
                
                
    def dfs(self, n, s, path, results):
        if s == '' and len(path) == n-1:
            # print(path)
            results.append(path[:])
            return
        
        
        for i in [1, 2]:
            if i > len(s):
                continue
            if int(s[:i])>n or int(s[:i]) == 0 or s[:i][0] == '0':
                continue
            if s[:i] in path:
                continue
            path.append(s[:i])
            self.dfs(n, s[i:], path, results)
            path.pop()
