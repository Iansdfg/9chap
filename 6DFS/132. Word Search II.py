DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if board == [] or words == []:
            return []
        words_set = set(words)
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i+1])
                
        results = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]
                self.dfs(
                    board, 
                    char,
                    row,
                    col,
                    set([(row,col)]),
                    words_set,
                    prefix_set,
                    results,
                    )
        return list(results)
        
    def dfs(self, board, word, row, col, visited, words_set, prefix_set, results):
        if word not in prefix_set:
            return
        
        if word in words_set:
            results.add(word)
        
        for x,y in DIRECTIONS:
            new_row = row + x
            new_col = col + y
            
            if not self.inside(board,new_row,new_col):
                continue
            if (new_row,new_col) in visited:
                continue
            
            visited.add((new_row,new_col))
            self.dfs(
                board, 
                word+board[new_row][new_col],
                new_row,
                new_col,
                visited,
                words_set,
                prefix_set,
                results,
                )
            visited.remove((new_row,new_col))
            
    def inside(self, board, row, col):
        return 0<= row < len(board) and 0<= col < len(board[0])
 
        
