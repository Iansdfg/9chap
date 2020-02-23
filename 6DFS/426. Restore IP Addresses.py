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
        
        if s == '' and len(path) == 4:
            print(path)
            results.append('.'.join(path))
            return
          
        for i in [1, 2, 3]:
            if i > len(s):
                return
            segment = s[:i]
            if int(segment) > 255:
                continue
            if str(int(segment)) != segment:
                continue
            path.append(segment)
            self.dfs(s[i:], path, results)
            path.pop()
