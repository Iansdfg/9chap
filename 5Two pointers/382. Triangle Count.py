class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s):
        # write your code here
        s.sort()
        ans = 0
        for i in range(len(s)):
            left, right = 0, i - 1 
            while left < right:
                if s[left] + s[right] > s[i]:
                    ans += right - left
                    right -= 1 
                else:
                    left += 1 
        return ans 

