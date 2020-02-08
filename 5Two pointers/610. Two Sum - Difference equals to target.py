class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        num_pos = []
        for pos, val in enumerate(nums):
            num_pos.append([val, pos]) 
        
        num_pos.sort()
        target = abs(target)
        right = 1 
        
        for left in range(len(num_pos)):
            while right < len(num_pos) and num_pos[right][0] - num_pos[left][0] < target:
                right += 1 
            if left != right and num_pos[right][0] - num_pos[left][0] == target:
                result = [num_pos[right][1]+1, num_pos[left][1]+1]
                result.sort()
                return result
