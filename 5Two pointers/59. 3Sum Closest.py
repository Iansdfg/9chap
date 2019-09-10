class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        length = len(numbers)
        res = 0
        minn = float('inf')
        for i in range(length):
            left, right =i+1, length-1
            while left<right:
                three_sum = numbers[i]+numbers[left]+numbers[right]
                if three_sum == target:
                    return target
                elif three_sum>target:
                    if minn > abs(three_sum-target):
                        res = three_sum
                        minn = abs(three_sum-target)
                    right-=1
                elif three_sum<target:
                    if minn > abs(three_sum-target):
                        res = three_sum
                        minn = abs(three_sum-target)
                    left+=1
        return res
