class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def dropEggs(self, n):
        # write your code here
        res, sum = 0, 0
        while sum<n:
            res += 1
            sum += res 
        return res 
        
