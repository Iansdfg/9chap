class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        right = 0
        while reader.get(right) <= target:
            right = right * 2 + 1
            
        print(right)
        left = 0
        while left + 1 < right:
            mid = (left + right)//2
            if reader.get(mid) < target:
                left = mid
            elif reader.get(mid) > target:
                right = mid
            elif reader.get(mid) == target:
                right = mid
                
        if reader.get(left) == target:
            return left
        elif reader.get(right) == target:
            return right
        return -1 
