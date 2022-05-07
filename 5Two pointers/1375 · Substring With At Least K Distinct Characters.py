class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def k_distinct_characters(self, s, k):
        # Write your code here
        left, ans = 0, 0
        char2cnt = dict()
        for right in range(len(s)):
            char2cnt[s[right]] = char2cnt.get(s[right], 0) + 1
            while left <= right and len(char2cnt) >= k:
                ans += len(s) - right
                char2cnt[s[left]] -= 1 
                if char2cnt[s[left]] == 0:
                    del char2cnt[s[left]]
                left += 1 
            
        return ans 


            
