class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        target = abs(target)
        numbers = [(pos+1, val) for pos, val in enumerate(nums)]
        numbers = sorted(numbers, key = lambda x:x[1])
        dic = {}
        for ele in numbers:
            # print(ele)
            if ele[1] not in dic:
                dic[ele[1]+target] = ele[0]
            else:
                return sorted([dic[ele[1]], ele[0]])
            
            
