class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if A==[]:
            return[[]]
        results = []
        self.dfs(A, k, target, 0, [], results)
        return results
        
    def dfs(self, A, k, target, index, path, results):
        if len(path)>k:
            return
        if target < 0:
            return
        if target == 0 and len(path)==k:
            results.append(path[:])
            return
        # print(path, results)
        for i in range(index, len(A)):
            path.append(A[i])
            self.dfs(A, k, target-A[i], i+1, path, results)
            path.pop()
        

        
class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if A==[]:
            return[[]]
        results = []
        self.dfs(A, k, target, 0, [], results)
        return results
        
    def dfs(self, A, k, target, index, path, results):
        if target == 0 and k == 0:
            results.append(path[:])
            return
        if k==0 or target < 0:
            return
        # print(path, results)
        for i in range(index, len(A)):
            path.append(A[i])
            self.dfs(A, k-1, target-A[i], i+1, path, results)
            path.pop()
        
