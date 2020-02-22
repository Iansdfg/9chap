class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0:
            n = -n 
            x = 1/x
        base = x
        ans = 1 
        while n:
            if n % 2:
                ans *= base
            base *= base
            n //= 2
        return ans 
