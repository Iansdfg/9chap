class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0 :
            x = 1 / x  
            n = -n
        # ans = 1
        # base = x
        # while n>0:
        #     if n%2:
        #         ans *= base
        #     base *= base
        #     n//=2
        # return ans
        if n == 0:
            return 1
        if n%2:
            ans = self.myPow(x, n//2)
            return ans*ans*x
        else:
            ans = self.myPow(x, n//2)
            return ans*ans
    
