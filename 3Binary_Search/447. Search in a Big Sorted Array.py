class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        bond = 1
        while reader.get(bond) <= target:
            bond = bond*2 

        start, end = 0, bond
        while start + 1 < end:
            mid = (start + end) // 2 
            if reader.get(mid) > target:
                end = mid 
            elif reader.get(mid) < target:
                start = mid 
            else: 
                end = mid 
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end 
        return -1




