class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        if dividend == 0 or divisor == 0:
            return 0
        if divisor == 1:
            return dividend
            
        is_neg = False 
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            is_neg = True
            
        divisor, dividend = abs(divisor), abs(dividend)
            
        res = 0
        while divisor <= dividend:
            summ, cnt = divisor, 1
            while summ + summ <= dividend:
                summ += summ
                cnt += cnt 
            dividend -= summ
            res += cnt
            
        res = min(2147483647, res)
        
        if is_neg:
            return -res
        return res 
