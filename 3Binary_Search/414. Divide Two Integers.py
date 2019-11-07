class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        max_val = 2147483647
        if dividend == 0:
            return 0
        if divisor == 1:
            return dividend
        
        is_neg = False 
        if (dividend < 0 and divisor > 0) or  (dividend > 0 and divisor < 0):
            is_neg = True
            
        dividend, divisor = abs(dividend), abs(divisor) 
        
        res = 0
        while divisor <= dividend:
            summ, cnt = divisor, 1
            while summ + summ < dividend:
                cnt += cnt
                summ += summ
            res += cnt
            dividend -= summ
            
            
        res = min(max_val, res)
        
        if is_neg:
            res = -res
        
        return res
            
        
        
