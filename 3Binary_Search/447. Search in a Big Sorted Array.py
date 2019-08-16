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
        right_bound = self.find_right_bound(reader, target)
        res_pos = self.binary_search(reader,  0, right_bound, target)
        return res_pos
        
    def find_right_bound(self, reader, target):
        index = 0
        while reader.get(index) <= target:
            index = index * 2 + 1
        return index
                
    def binary_search(self, reader, start, end, target):
        
        while start+1<end:
            m = (start + end)//2
            if reader.get(m)>target:
                end = m
            elif reader.get(m)<target:
                start = m 
            else:
                end = m
        
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        else:
            return -1
               
