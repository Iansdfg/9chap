class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def three_sum_closest(self, numbers, target):
        # write your code here
        numbers.sort()
        min_val, ans = float('inf'), None
        for pos in range(len(numbers)):
            start, end = pos + 1, len(numbers) - 1
            while start < end:
                value = numbers[pos] + numbers[start] + numbers[end]

                if value > target:
                    end -= 1 
                elif value < target:
                    start += 1 
                else:
                    return value
                if abs(value - target) < min_val:
                    min_val = abs(value - target)
                    ans = value
        return ans
            
