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
