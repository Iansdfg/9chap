class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s):
        # Write your code here
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] == s[end]:
                start += 1 
                end -= 1 
            else:
                return self.is_palindrome(s, start + 1, end) or self.is_palindrome(s, start, end - 1)
        return True

    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] == s[end]:
                start += 1 
                end -= 1 
            else:
                return False 
        return True
