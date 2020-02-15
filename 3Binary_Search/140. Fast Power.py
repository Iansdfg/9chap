class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            x = 1/x
            n = -n
        base = x 
        ans = 1 
        while n:
            if n % 2 == 1:
                ans *= base
            base *= base 
            n = n // 2 
        return ans 
            
