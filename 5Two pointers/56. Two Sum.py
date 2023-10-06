from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        num_pos = {}
        for pos, num in enumerate(numbers):
            if num in num_pos:
                return [num_pos[num], pos]
            num_pos[target - num] = pos
            
from typing import (
    List,
)

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        # write your code here
        new_nums = []
        for pos, num in enumerate(numbers):
            new_nums.append((num, pos))
        new_nums.sort()
        print(new_nums)
        left, right = 0, len(numbers) - 1 
        while left < right:
            if new_nums[left][0] + new_nums[right][0] < target:
                left += 1 
            elif new_nums[left][0] + new_nums[right][0] > target:
                right -= 1
            else:
                big = max(new_nums[left][1], new_nums[right][1])
                small = min(new_nums[left][1], new_nums[right][1])
                
                return [small, big]
        return [-1, -1]
