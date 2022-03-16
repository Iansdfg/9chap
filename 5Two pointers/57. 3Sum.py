class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def three_sum(self, numbers):
        # write your code here
        numbers = sorted(numbers)
        results = []
        for pos, val in enumerate(numbers):
            if pos > 0 and numbers[pos] == numbers[pos - 1]:
                continue
            results += self.two_sum(numbers, pos + 1, len(numbers) - 1, val)
        return results

    def two_sum(self, numbers, start, end, target):
        neg_target = target * -1
        res = []
        last = None
        while start < end:
            val = numbers[start] + numbers[end]
            if val > neg_target:
                end -= 1
            elif val < neg_target:
                start += 1 
            else:
                if (numbers[start], numbers[end]) != last:
                    res.append((target, numbers[start], numbers[end]))
                last = (numbers[start], numbers[end])
                end -= 1
                start += 1 
        return res 
