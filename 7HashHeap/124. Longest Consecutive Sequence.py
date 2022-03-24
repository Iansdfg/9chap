class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longest_consecutive(self, num):
        # write your code here
        visited = set(num)
        res, length = 0, 0
        for number in num:
            if number in visited:
                visited.remove(number)
                length = 1
                left = number - 1
                right = number + 1 
                while left in visited:
                    visited.remove(left)
                    left -= 1 
                    length += 1
                while right in visited:
                    visited.remove(right)
                    right += 1
                    length += 1
            res = max(res, length)
        return  res

                


