class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers):
        # write your code here
        numbers.sort()
        res = []
        last_pair = None
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, len(numbers) - 1
            while left < right:
                summ = numbers[i] + numbers[left] + numbers[right]
                if summ < 0:
                    left += 1 
                elif summ > 0:
                    right -= 1 
                else:
                    if [numbers[i], numbers[left], numbers[right]] != last_pair:
                        res.append([numbers[i], numbers[left], numbers[right]])
                        last_pair = [numbers[i], numbers[left], numbers[right]]
                    left += 1 
                    right -= 1

        return res

