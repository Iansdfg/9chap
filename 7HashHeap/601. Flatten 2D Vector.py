from heapq import heappush, heappop

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.vec2d = vec2d
        self.heap = []
        
        for index, array in enumerate(vec2d):
            if len(array) == 0:
                continue
            heappush(self.heap, (vec2d[index][0], index, 0))
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        curr_val, curr_row, curr_col = heappop(self.heap)
        if curr_col + 1 >= len(self.vec2d[curr_row]):
            return curr_val
        next_col = curr_col + 1 
        heappush(self.heap, (self.vec2d[curr_row][next_col], curr_row, next_col))
        return curr_val
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        return len(self.heap) != 0
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
