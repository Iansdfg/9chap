import heapq
class Solution:

    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergek_sorted_arrays(self, arrays):
        # write your code here
        heap = []
        res = []
        for array in arrays:
            if not array:
                continue
            heapq.heappush(heap, (array[0], array)) 

        while heap:
            curr_val, curr_array = heapq.heappop(heap)
            res.append(curr_val)
            curr_array.pop(0)
            if not curr_array:
                continue
            heapq.heappush(heap, (curr_array[0], curr_array))
            
        return res 


        
