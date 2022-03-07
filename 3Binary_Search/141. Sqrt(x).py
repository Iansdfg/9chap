class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid**2 > x:
                end = mid 
            else:
                start = mid
        if start**2 == x:
            return start
        if end ** 2 == x:
            return end
        return min(start, end)
            

