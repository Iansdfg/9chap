class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        word_set = set()
        count = 0
        for char in s:
            if char not in word_set:
                word_set.add(char)
            else:
                count += 1 
                word_set.discard(char)
        return min(count*2 + 1, len(s))
            
        
