class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a, target, k):
        # write your code here
        upper = self.find_upper(a, target)
        lower = upper - 1 
        res = []
        for _ in range(k):
            if self.lower_closer(a, target, lower, upper):
                res.append(a[lower])
                lower -= 1 
            else:
                res.append(a[upper])
                upper += 1 
        return res


    def find_upper(self, a, target):
        start, end = 0, len(a)-1 
        while start + 1 < end:
            mid = (start + end ) // 2 
            if a[mid] < target:
                start = mid 
            else:
                end = mid 
        if a[start] >= target:
            return start
        if a[end] >= target:
            return end
        return len(a)
    
    def lower_closer(self,a, target, lower, upper):
        if lower < 0:
            return False 
        if upper >= len(a):
            return True
        return target - a[lower] <= a[upper] - target
        
         
#######################10/18/2022#######################
            
            
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def k_closest_numbers(self, a: List[int], target: int, k: int) -> List[int]:
        # write your code here
        if k == 0:
            return []
        closest_pos = self.closest_number(a, target)
        res = [a[closest_pos]]
        left, right = closest_pos - 1,closest_pos + 1
        while len(res) < k:
            if self.left_closer(a, left, right, target):
                res.append(a[left])
                left -= 1 
            else:
                res.append(a[right])
                right += 1 
        return res 


    def left_closer(self, a, left, right, target):
        if right >= len(a):
            return True  
        return abs(a[left] - target) <= abs(a[right] - target)

    def closest_number(self, a, target):
        start, end = 0, len(a) - 1 
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] > target:
                end = mid 
            elif a[mid] < target:
                start = mid 
            else:
                return mid
        if abs(a[start] - target) <= abs(a[end] - target):
            return start
        else:
            return end





