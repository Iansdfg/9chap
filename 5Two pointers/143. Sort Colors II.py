class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors, k):
        # write your code here
        # why use k, its not index, its color number so we need use k intsead of k+1/k-1
        self.rainbow_sort(colors, 1, k, 0, len(colors) - 1)


    def rainbow_sort(self, colors, form_color, to_color, from_index, to_index):
        if from_index == to_index or form_color == to_color:
            return

        left, right = from_index, to_index
        pivot = (form_color + to_color) // 2 

        while left <= right:
            #use <= and > cam seperate colors 
            while left <= right and colors[left] <= pivot:
                left += 1 
            while left <= right and colors[right] > pivot:
                right -= 1 
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1 
                right -= 1 

        
        self.rainbow_sort(colors, k, form_color, pivot, from_index, right)
        self.rainbow_sort(colors, k, pivot + 1, to_color, left, to_index)

