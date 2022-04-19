class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
             we will sort your return value in output
    """
    def four_sum(self, numbers, target):
        # write your code here
        numbers.sort()
        res = []
        last_pari = None 
        for first in range(len(numbers)):
            if first > 0 and numbers[first] == numbers[first - 1]:
                continue
            for second in range(first + 1, len(numbers)):
                if second > first + 1 and numbers[second] == numbers[second - 1]:
                    continue
                left, right = second + 1, len(numbers) - 1 
                while left < right:
                    four_sum = numbers[first] + numbers[second] + numbers[left] + numbers[right]
                    if four_sum > target:
                        right -= 1 
                    elif four_sum < target:
                        left += 1 
                    else:
                        if [numbers[first], numbers[second], numbers[left], numbers[right]] != last_pari:
                            res.append([numbers[first], numbers[second], numbers[left], numbers[right]])
                            last_pari = [numbers[first], numbers[second], numbers[left], numbers[right]]
                        left += 1 
                        right -= 1 
        return res 

