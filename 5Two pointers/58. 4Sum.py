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
        print(numbers)
        res = []
        for fir_pos in range(len(numbers)):
            if fir_pos > 0 and numbers[fir_pos] == numbers[fir_pos - 1]:
                continue
            for sec_pos in range(fir_pos + 1, len(numbers)):
                if sec_pos > fir_pos + 1 and numbers[sec_pos] == numbers[sec_pos - 1]:
                    continue
                start, end = sec_pos + 1, len(numbers) - 1
                while start < end:
                    print([numbers[fir_pos], numbers[sec_pos], numbers[start], numbers[end]])   
                    four_sum = numbers[fir_pos] + numbers[sec_pos] + numbers[start] + numbers[end]
                    if four_sum > target:
                        end -= 1 
                    elif four_sum < target:
                        start += 1 
                    else:
                        res.append([numbers[fir_pos], numbers[sec_pos], numbers[start], numbers[end]])
                        start += 1 
                        end -= 1 
                    #two while look remove redundency inside two sum
                    while end > start and start > sec_pos + 1 and numbers[start]  == numbers[start - 1]:
                        start += 1 
                    while end > start and end < len(numbers) - 1 and numbers[end]  == numbers[end + 1]:
                        end -= 1 
                        
        return res
