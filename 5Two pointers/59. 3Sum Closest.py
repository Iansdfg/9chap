class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        numbers.sort()
        mini = float('inf')
        res = 0
        for i in range(len(numbers)):
            left, right = i+1 , len(numbers) - 1 
            while left < right:
                
                three_sum = numbers[i] + numbers[left] + numbers[right]
                
                if three_sum > target:
                    if abs(three_sum - target) < mini:
                        mini = abs(three_sum - target)
                        res = three_sum
                    right -= 1 
                    
                elif three_sum < target:
                    if abs(three_sum - target) < mini:
                        mini = abs(three_sum - target)
                        res = three_sum
                    left += 1 
                    
                elif three_sum == target:
                    return three_sum
                    
        return res 
                
