class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n<0:
            n = -n 
            x = 1/x 
            
        base, last_ans = x, 1 
        while n:
            print(base, last_ans, n)
            if n % 2:
                last_ans *= base
            base *= base 
            n //= 2
        return last_ans 
