class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        results = []
        
        for pos in range(len(numbers)):
            if pos > 0 and numbers[pos] == numbers[pos - 1]:
                continue
            
            left, right = pos + 1, len(numbers) - 1 
            while left < right:
                three_sum = numbers[pos] + numbers[left] + numbers[right]
                if three_sum == 0:
                    results.append([numbers[pos], numbers[left],  numbers[right]])
                    left += 1 
                    right -= 1 
                elif three_sum > 0:
                    right -= 1 
                elif three_sum < 0:
                    left += 1 
                    
                while left < right and left > pos + 1 and numbers[left] == numbers[left - 1]:
                    left += 1 
                while left < right and right < len(numbers) - 1  and numbers[right] == numbers[right + 1]:
                    right -= 1 
                    
        return results
                
