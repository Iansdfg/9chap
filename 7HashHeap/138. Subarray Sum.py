class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        sum2index = {0:-1}
        new_sum = 0
        for pos, num in enumerate(nums):
            new_sum += num
            sum2index[new_sum] = pos
            if new_sum in sum2index:
                return sum2index[new_sum], pos - 1
        return -1, -1
