class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n<0:
            x = 1/x
        n = abs(n)
        ans = 1
        base = x
        while n:
            if n%2:
                ans*=base
            n//=2 
            base*=base
            
        return ans 
        
