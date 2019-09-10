class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S.sort()
        ans = 0
        for i in range(len(S)):
            left, right = 0,i-1
            while left<right:
                if S[left]+S[right]>S[i]:
                    ans += right-left
                    right-=1
                else:
                    left+=1 
        return ans
                
