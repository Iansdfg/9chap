class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers):
        # write your code here
        numbers.sort()
        print(numbers)
        res = []
        last = None 
        for i in range(len(numbers)):
            # 解决外部循环去重
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                three_sum = numbers[i] + numbers[left] +  numbers[right] 
                if three_sum > 0:
                    right -= 1 
                elif three_sum < 0:
                    left += 1 
                else:
                    # 解决2 sum 去重
                    if [numbers[i], numbers[left], numbers[right]] != last:
                        res.append([numbers[i], numbers[left], numbers[right]])
                        last = [numbers[i], numbers[left], numbers[right]]
                    left += 1 
                    right -= 1
        return res 


