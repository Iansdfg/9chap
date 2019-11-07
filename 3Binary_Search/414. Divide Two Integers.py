class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        if dividend == 0:
            return 0
        
        if divisor == 0:
            return 0
            
        if divisor == 1:
            return dividend
            
        is_neg = False
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            is_neg = True
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        while divisor <= dividend:
            cnt, summ = 1, divisor
            while summ + summ < dividend:
                summ += summ
                cnt += cnt
            res += cnt
            dividend -= summ
            
        res = min(2147483647, res)
        
        if is_neg:
            return -res
        return res
                
            
