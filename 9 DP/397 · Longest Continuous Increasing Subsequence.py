class Solution:
    """
    @param a: An array of Integer
    @return: an integer
    """
    def longest_increasing_continuous_subsequence(self, a):
        # write your code here
        if not a:
            return 0
        longest, inc, dec = 1, 1, 1
        for i in range(1, len(a)):
            if a[i] > a[i-1]:
                dec += 1 
                inc = 1 
            elif a[i] < a[i-1]:
                inc += 1 
                dec = 1 
            else:
                inc = 1 
                dec = 1 
            longest = max(longest, max(inc, dec))
        return longest



