class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        numbers.sort()
        res = []
        print(numbers)
        for first_pos in range(len(numbers)):
            if first_pos > 0 and numbers[first_pos] == numbers[first_pos - 1]:
                    continue
            
            for second_pos in range(first_pos+1, len(numbers)):
                if second_pos > first_pos+1 and numbers[second_pos] == numbers[second_pos - 1]:
                    continue
                
                left, right = second_pos + 1, len(numbers)-1
                while left < right:
                    four_sum = numbers[first_pos] + numbers[second_pos] + numbers[left] + numbers[right]
                    if four_sum == target:
                        res.append([numbers[first_pos], numbers[second_pos], numbers[left], numbers[right]])
                        left += 1 
                        right -= 1 
                    elif four_sum > target:
                        right -= 1 
                    elif four_sum < target:
                        left += 1 
                        
                    while left < right and left > second_pos+1 and numbers[left] == numbers[left - 1]:
                        left += 1 
                    while left < right and right < len(numbers) - 1 and numbers[right] == numbers[right + 1]:
                        right -= 1 
                  
        return res 
                    
