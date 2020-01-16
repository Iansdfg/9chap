class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        graph = self.built_graph(words)
        print(graph)
        # order = self.topological_sort()
        return '' 
        
    def built_graph(self, words):
        char_to_next = {}
        
        # initiate graph
        for word in words:
            for char in word:
                if char not in char_to_next:
                    char_to_next[char] = set()
                    
        n = len(words)
        for pos_word in range(n-1):
            for pos_char in range(min(len(words[pos_word]), len(words[pos_word + 1]))):
                # to avoid same prefix, if not same, 
                if words[pos_word][pos_char] != words[pos_word+1][pos_char]:
                    char_to_next[words[pos_word][pos_char]].add(words[pos_word+1][pos_char])
                    break
                
        return char_to_next
            
                    
