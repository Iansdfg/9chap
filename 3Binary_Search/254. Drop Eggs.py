class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def dropEggs(self, n):
        # write your code here
        right_bound = 1;
        while (right_bound * (right_bound + 1) / 2 < n):
            right_bound = right_bound * 2
        
        start,end  = 1, right_bound
        while start + 1 < end:
            mid = (start + end)// 2
            if mid * (mid + 1) / 2 >= n:
                end = mid
            else:
                start = mid

        if start * (start + 1) / 2 >= n:
            return start
        else:
            return end
