from typing import (
    List,
)

class Solution:
    """
    @param a: An integers array.
    @return: return any of peek positions.
    """
    def find_peak(self, a: List[int]) -> int:
        # write your code here
        if not a:
            return 0
        start, end = 1, len(a) - 2
        #需要考虑： peak 有没有可能在第一位和最后一位

        while start + 1 < end:
            mid = (start + end) //2
            if a[mid] > a[mid-1] and a[mid] > a[mid+1]:
                return mid

            elif a[mid] > a[mid-1] and a[mid] < a[mid+1]:
                start = mid 
            elif a[mid] < a[mid-1] and a[mid] > a[mid+1]:
                end = mid 
        
        if a[start] > a[end]:
            return start
        else:
            return end
 

