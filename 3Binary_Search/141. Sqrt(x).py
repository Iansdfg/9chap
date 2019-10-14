class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left, right = 1, x
        while left+1<right:
            mid = (left+right)//2
            if mid**2 > x:
                right = mid
            elif mid**2 < x:
                left = mid
            else:
                return mid
                
        if left**2<x:
            return left 
        else:
            return right
        
            
