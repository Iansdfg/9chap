class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a):
        # write your code here
        self.quick_sort(a, 0, len(a) - 1)
        

    def quick_sort(self, a, start, end):
        print(start, end, a)
        if start >= end:
            return

        left, right = start, end

        mid = (left + right)//2
        pivot = a[mid]
        while left <= right:
            # quick sort have to use < insted of others
            # or left and right pointer cannot go to the boundry 
            # thus cause run time error
            while left <= right and a[left] < pivot:
                left += 1
            while left <= right and a[right] > pivot:
                right -= 1 
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1 
                right -= 1
        
        self.quick_sort(a, start, right)
        self.quick_sort(a, left, end)
