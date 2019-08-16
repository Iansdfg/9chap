"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        index = 0
        while reader.get(index) <= target:
            index = index * 2 + 1
            
        start, end = 0, index
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            elif reader.get(mid) >= target:
                end = mid
                
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1
            
            
        
        
          
