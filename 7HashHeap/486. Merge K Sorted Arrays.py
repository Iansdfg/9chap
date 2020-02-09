from heapq import heappop, heappush 

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        heap = []
        
        for pos_x, array in enumerate(arrays):
            if len(array) == 0:
                continue
            heappush(heap, (array[0], pos_x, 0))
            
        result = []
        while heap:
            curr_val, curr_pos_x, curr_pos_y = heappop(heap)
            result.append(curr_val)
            if curr_pos_y + 1 < len(arrays[curr_pos_x]):
                heappush(heap, (arrays[curr_pos_x][curr_pos_y + 1], curr_pos_x, curr_pos_y + 1))
            
        return result
            
            
            
        
