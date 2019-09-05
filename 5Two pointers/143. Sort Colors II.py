class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        left = 0
        for i in range(1,k+1):
            new_left = self.sort(colors, i, left)
            # print(i,colors)
            left = new_left
        
        
        
    def sort(self, colors, target, left):
        left, right = 0, len(colors)-1
        
        while left<=right:
            while left<=right and colors[left]<=target:
                left+=1
                
            while left<=right and colors[right]>target:
                right-=1
            
            if left<=right:
                colors[right],colors[left] = colors[left],colors[right]
                left+=1
                right-=1
                
        return left
                
