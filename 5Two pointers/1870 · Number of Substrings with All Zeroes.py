class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def string_count(self, str):
        # Write your code here.
        cnt = 0
        ans = 0
        for num in str:
            if num == "0":
                cnt += 1 
            else:
                ans += (cnt * (cnt + 1)) //2
                cnt = 0

        if cnt != 0:
            ans += (cnt * (cnt + 1)) //2
        return ans 
