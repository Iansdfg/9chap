
DIRECTIONS =[(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if board is None or len(board) == 0:
            return []
            
        word_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
               prefix_set.add(word[:i+1])
               
        resultes = set()
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]
                self.dfs(
                    board, 
                    row,
                    col,
                    char,
                    word_set,
                    prefix_set,
                    set([(row, col)]),
                    resultes,
                )
                    
        return list(resultes)
                
                
    def dfs(self, board, row, col, word, word_set, prefix_set, visited, resultes):
        if word not in prefix_set:
            return
        if word in word_set:
            resultes.add(word)
            
        for delta_row, delta_col in DIRECTIONS:
            row_ = row + delta_row
            col_ = col + delta_col
            
            if not self.inside(board, row_, col_):
                continue
            if (row_, col_) in visited:
                continue
            
            visited.add((row_, col_))
            self.dfs(
                    board, 
                    row_,
                    col_,
                    word + board[row_][col_],
                    word_set,
                    prefix_set,
                    visited,
                    resultes,
                )
            visited.remove((row_, col_))
             
    def inside(self, board, row, col):
        return 0<=row<len(board) and 0<=col<len(board[0])
            
            
        
        
        
            
        
