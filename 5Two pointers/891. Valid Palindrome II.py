class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def valid_palindrome(self, s):
        # Write your code here
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            else:
                return self.helper(s, left + 1, right) or self.helper(s, left, right - 1) 

        return True

    def helper(self, s, left, right):
        while left <= right:
            if s[left] == s[right]:
                left += 1 
                right -= 1 
            else:
                return False 
        return True

