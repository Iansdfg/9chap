class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S.sort()
        result = 0
        for pos in range(len(S)):
            left, right = 0, pos - 1  
            while left < right:
                if S[left] + S[right] > S[pos]:
                    result += right - left
                    right -= 1 
                else:
                    left += 1 
        return result
