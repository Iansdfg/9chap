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
            
