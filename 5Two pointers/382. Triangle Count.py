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
                
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S.sort()
        S.reverse()
        length = len(S)
        res = 0
        for pos, num in enumerate(S):
            left = pos+1
            res+=self.greater_than(S[left:], num)
        return res
    
    
    def greater_than(self, nums, target):
        nums.sort()
        ans = 0
        left, right = 0, len(nums)-1
        while left<right:
            two_sum = nums[left] + nums[right]
            if two_sum>target:
                ans+=right-left
                right-=1
            else:
                left+=1
        return ans
