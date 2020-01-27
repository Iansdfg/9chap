class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, string):
        # write your code here
        results = []
        self.dfs(n, string, 0, [], results)
        summ = 0
        for ele in results[0]:
            summ += int(ele)
        return (n*(n+1))//2 - summ

    def dfs(self, n, string, index, path, results):
        if len(path) == n-1 and string == '':
            results.append(path[:])
            return
        
        for i in range(1, 3):
            if i > len(string):
                return
            
            num = string[:i]
            if num in path or int(num)<1 or int(num)>n:
                continue
            if len(num) == 2 and num[0] == '0':
                continue
            
            path.append(num)
            self.dfs(n, string[i:], 0, path, results)
            path.pop()
            
        
        
        
