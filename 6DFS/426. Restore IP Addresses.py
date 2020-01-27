class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        if len(s)<4:
            return []
        results = []
        self.dfs(s, [], results)
        return results
        
    def dfs(self, s, path, results):
        if s == '' and len(path) == 4:
            results.append('.'.join(path[:]))
            return
        
        for i in range(1, 4):
            if i > len(s):
                return
            ip_part = s[:i]
            if int(ip_part) > 255:
                continue
            if str(int(ip_part)) != ip_part:
                continue
            path.append(ip_part)
            self.dfs(s[i:], path, results)
            path.pop()
        
