class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        
        if x>=1:
            start, end = 1, float(x)
        else:
            start, end = float(x), 1
            
        while start + 1e-10 < end:
            mid = (start + end) / 2
            if mid * mid > x:
                end = mid 
            elif mid * mid < x:
                start = mid 
            else:
                return mid 
                
        if end*end <= x:
            return end 
        return start
