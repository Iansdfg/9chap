class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        
        rows, cols = len(image), len(image[0])
        if rows == 0 or cols == 0:
            return 0
        
        left = self.find_left(image, 0, y)
        right = self.find_right(image, y, cols-1)
        up = self.find_up(image, 0, x)
        down = self.find_down(image, x, rows-1)
        print(left, right, up, down)
        return (down-up+1)*(right-left+1)
        
    def find_up(self, image, start, end):
        print(start, end)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.black_in_row(image, mid):
                end = mid 
            else:
                start = mid 
            print(start, end, mid, self.black_in_row(image, mid))
                
        if self.black_in_row(image, start):
            return start
        return end
        
    def find_down(self, image, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if self.black_in_row(image, mid):
                start = mid 
            else:
                end = mid 
                
        if self.black_in_row(image, end):
            return end
        return start
        
    def black_in_row(self, image, row):
        for col in range(len(image[0])):
            if image[row][col] == '1':
                return True
        return False
            
    def find_left(self,image, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if self.black_in_col(image, mid):
                end = mid 
            else:
                start = mid 
                
        if self.black_in_col(image, start):
            return start
        return end
        
    def find_right(self,image, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if self.black_in_col(image, mid):
                start = mid 
            else:
                end = mid 
                
        if self.black_in_col(image, end):
            return end
        return start
        
    def black_in_col(self, image, col):
        for row in range(len(image)):
            if image[row][col] == '1':
                return True
        return False
        
        
