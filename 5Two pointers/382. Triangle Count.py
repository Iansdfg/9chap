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
                #如果S[left] + S[right] > S[i]，说明三者可以构成三角形。
                #与此同时，最小边的索引为left+1, left+2,...,right-1时，都能与S[right]和S[i]构成三角形。
                #所以满足条件的三角形找到了right-left个。然后right指针左移进入下一轮。
                if s[left] + s[right] > s[i]:
                    res += right - left
                    right -= 1 
                else:
                    left += 1 
        return res 

