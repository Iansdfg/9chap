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
        
         
