class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        results = []
        self.dfs(s, [], results)
        return results
        
    def dfs(self, s, path, results):
        if len(path) > 4:
            return
        
        if s == '' and len(path) == 4:
            results.append('.'.join(path))
            return
        
        for i in range(1,4):
            if i > len(s):
                return
            seg = s[:i] 
            if int(seg) > 255:
                return
            if str(int(seg)) != seg:
                return
            path.append(seg)
            self.dfs(s[i:], path, results)
            path.pop()
