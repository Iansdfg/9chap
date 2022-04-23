class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s):
        # write your code here
        max_val = 0
        index = 0
        for i in range(len(s)):
            length = max(self.check_palindrome(s, i, i), self.check_palindrome(s, i, i+1))
            if length > max_val:
                max_val = length
                index = i
        if max_val % 2:
            return s[index - max_val/2: index + max_val/2 + 1]
        else:
            return s[index - max_val/2 + 1:index + max_val/2 + 1]

    def check_palindrome(self, s, start, end):
        left, right = start, end 
        
        while True:
            if left < 0 or right >= len(s):
                break 
            if s[left] != s[right]:
                break
            left -= 1 
            right += 1 
        return right - left - 1 
