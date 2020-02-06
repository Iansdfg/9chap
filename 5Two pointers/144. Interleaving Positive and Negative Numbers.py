class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        
        pos, neg = 0, 0
        
        for num in A:
            if num > 0: 
                pos += 1 
            else:
                neg += 1 
                
        if pos == neg:
            self.pos_neg_equal(A)
        elif pos > neg:
            self.pos_more(A)
        else:
            self.neg_more(A)
            
            
    def pos_neg_equal(self, A):
            
        start, end = 0, len(A) - 1
                
        while start <= end: 
            while start <= end and A[start] < 0:
                start += 1 
            while start <= end and A[end] > 0:
                end -= 1 
            if start <= end: 
                A[start], A[end] = A[end], A[start] 
                start += 1 
                end -= 1 
        
        start, end = 1, len(A) - 2
        while start < end:
            A[start], A[end] = A[end], A[start] 
            start, end = start + 2, end - 2
            
            
    def pos_more(self, A):
            
        start, end = 0, len(A) - 1
                
        while start <= end: 
            while start <= end and A[start] > 0:
                start += 1 
            while start <= end and A[end] < 0:
                end -= 1 
            if start <= end: 
                A[start], A[end] = A[end], A[start] 
                start += 1 
                end -= 1 
        
        start, end = 1, len(A) - 1
        while start < end:
            A[start], A[end] = A[end], A[start] 
            start, end = start + 2, end - 2
            
            
    def neg_more(self, A):
            
        start, end = 0, len(A) - 1
                
        while start <= end: 
            while start <= end and A[start] < 0:
                start += 1 
            while start <= end and A[end] > 0:
                end -= 1 
            if start <= end: 
                A[start], A[end] = A[end], A[start] 
                start += 1 
                end -= 1 
        
        start, end = 1, len(A) - 1
        while start < end:
            A[start], A[end] = A[end], A[start] 
            start, end = start + 2, end - 2
                
                    
        
            
