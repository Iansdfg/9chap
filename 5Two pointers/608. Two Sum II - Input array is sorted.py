class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        dic = dict()
        for pos, val in enumerate(nums):
            if val not in dic:
                dic[target-val] = pos+1
            else:
                return [dic[val], pos+1]

class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        l,r = 0, len(nums)-1
        while l<r:
            summ = nums[l] + nums[r]
            if summ == target:
                return [l+1,r+1]
            elif summ<target:
                l+=1
            elif summ>target:
                r-=1
        return []
