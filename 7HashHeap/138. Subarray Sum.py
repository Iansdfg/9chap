class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prifix_sum_to_id = dict()
        prifix_sum_to_id[0] = -1 
        prifix_sum = 0
        for pos, val in enumerate(nums):
            prifix_sum += val
            if prifix_sum in prifix_sum_to_id:
                return [prifix_sum_to_id[prifix_sum]+1, pos]
            prifix_sum_to_id[prifix_sum] = pos
        return [-1, -1]
            
            
            
