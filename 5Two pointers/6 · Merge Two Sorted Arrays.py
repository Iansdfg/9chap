class Solution:
    """
    @param a: sorted integer array A
    @param b: sorted integer array B
    @return: A new sorted integer array
    """
    def merge_sorted_array(self, a, b):
        # write your code here
        if not a or not b:
            return a or b
        upper, lower = 0, 0
        res = []
        while upper < len(a) and lower < len(b):
            if a[upper] < b[lower]:
                res.append(a[upper])
                upper += 1 
            else:
                res.append(b[lower])
                lower += 1 

        if upper >= len(a):
            res += b[lower:]
        elif lower >= len(b):
            res += a[upper:]
        return res 

            
