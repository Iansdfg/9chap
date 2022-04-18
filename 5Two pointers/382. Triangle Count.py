class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s):
        # write your code here
        s.sort()
        cnt = 0 
        for i in range(2, len(s)):
            left, right = 0, i - 1 
            while left < right:
                if s[left] + s[right] > s[i]:
                    cnt += right - left
                    right -= 1 
                else:
                    left += 1 
        return cnt 
                    
class Solution:
    """
    @param s: A list of integers
    @return: An integer
    """
    def triangle_count(self, s):
        # write your code here
        s.sort()
        res = 0
        for i in range(len(s) - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if s[left] + s[right] > s[i]:
                    res += right - left
                    right -= 1 
                else:
                    left += 1 
        return res 

