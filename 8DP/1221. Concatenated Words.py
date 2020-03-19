class Solution:
    """
    @param words: List[str]
    @return: return List[str]
    """
    def findAllConcatenatedWordsInADict(self, words):
        # write your code here
        words.sort(key = lambda x: len(x))
        words.reverse()
        results = []
        dic = set(words)
        
        for word in words:
            dic.discard(word)
            if word == '':
                continue
            if self.word_break(word, dic):
                results.append(word)
    
        return results
        
    def word_break(self, word, dic):
        n = len(word)
        dp = [0] * (n + 1)
        dp[0] = 1 
        
        for i in range(n + 1):
            for j in range(i):
                if not dp[j]:
                    continue
                if word[j:i] in dic:
                    dp[i] = 1 
                    
        return dp[-1]
                    
                    
                    
                    
                    
                    
                    
                    
                
