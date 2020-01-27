class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        results = []
        self.dfs(n, str, [], results)
        summ = 0
        for ele in results[0]:
            summ += int(ele) 
            
        return (n*(n+1))//2 - summ
        
        
    def dfs(self, n, str, path, results):
        if str == '' and len(path) == n-1:
            results.append(path[:])
            return
        
        for i in range(1, 3):
            if i>len(str):
                return
            num = str[:i]
            if num in path or int(num) < 1 or int(num) > n:
                continue
            if num[0] == '0':
                continue
            path.append(num)
            self.dfs(n, str[i:], path, results)
            path.pop()
