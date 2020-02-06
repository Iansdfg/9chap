class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        color_start, color_end = 1, k 
        index_start, index_end = 0, len(colors) - 1 
        self.rainbow_sort(colors, color_start, color_end, index_start, index_end)
        
        
    def rainbow_sort(self, colors, color_start, color_end, index_start, index_end):
        
        if index_start == index_end or color_start == color_end:
            return
        
        color_mid = (color_start + color_end) // 2 
        
        left, right = index_start, index_end
        
        while left <= right:
            while left <= right and colors[left] <= color_mid:
                left += 1
            while left <= right and colors[right] > color_mid:
                right -= 1
                
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1 
                
        self.rainbow_sort(colors, color_start, color_mid, index_start, right)
        self.rainbow_sort(colors, color_mid + 1, color_end, left , index_end)
    
