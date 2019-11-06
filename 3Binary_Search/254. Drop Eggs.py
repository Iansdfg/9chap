class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def dropEggs(self, n):
        # write your code here
        # in short find smallest k that k*(k+1)>=n
        end = 1 
        while end * (end + 1) / 2 < n:
            end *= 2
        
        start = 0
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * (mid + 1) / 2  >= n:
                end = mid
            else:
                start = mid
            
        if start * (start + 1) / 2 >= n:
            return start
        else:
            return end
